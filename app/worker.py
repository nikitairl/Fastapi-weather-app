from celery import Celery
from celery.schedules import crontab

from . import crud, main, weather_api, config


settings = config.get_settings()


REDIS_URL = settings.redis_url

celery_app = Celery(__name__)


# docker run -it -p 6379:6379 redis bash
# celery --app app.worker.celery_app worker
# --beat -s celerybeat-schedule --loglevel INFO


celery_app.conf.broker_url = REDIS_URL
celery_app.conf.result_backend = REDIS_URL


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute="*/10"),
        get_weather_apis.s(),
    )


@celery_app.task
def get_weather_apis():
    database = next(main.get_db())
    cities = crud.get_cities(database)

    for city in cities:
        weather_data = weather_api.fetch_weather_data(city.lat, city.lon)
        weather_api.update_city_with_weather(database, city, weather_data)
