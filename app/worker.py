import requests
from celery import Celery
from celery.schedules import crontab
from sqlalchemy.orm import Session

from . import crud, main, models


celery_app = Celery(__name__)
settings = {
    'broker_url': 'redis://localhost:6379',
}


# docker run -it -p 6379:6379 redis bash
# celery --app app.worker.celery_app worker --beat -s celerybeat-schedule --loglevel INFO


celery_app.conf.broker_url = settings['broker_url']
celery_app.conf.result_backend = settings['broker_url']


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute="*/1"),
        print_all_cities.s(),
    )


@celery_app.task
def print_all_cities():
    database = next(main.get_db())
    cities = crud.get_cities(database)

    for city in cities:
        print(list(city.__dict__.values()))


@celery_app.task
def get_weather_apis():
    database = next(main.get_db())
    cities = crud.get_cities(database)

    for city in cities:
        weather_data = fetch_weather_data(city.lat, city.lon)
        update_city_with_weather(database, city, weather_data)


def fetch_weather_data(lat, lon):
    API_key = "729b98baef5347afc700bc1ba8077b5d"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
    request_data = requests.get(url)
    return request_data.json()


def update_city_with_weather(
    database: Session,
    city: models.City,
    weather_data: dict
):
    # Update the city model with weather data
    city.data = weather_data
    city.tmp = weather_data["main"]["temp"]
    # Update other fields as needed
    database.add(city)
    database.commit()
    return city
