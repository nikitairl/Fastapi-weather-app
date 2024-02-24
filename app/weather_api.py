import requests
from sqlalchemy.orm import Session

from . import models, config


settings = config.get_settings()


def fetch_weather_data(lat, lon):
    API_key = settings.api_key
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_key}"
    request_data = requests.get(url)
    return request_data.json()


def update_city_with_weather(
    database: Session,
    city: models.City,
    weather_data: dict
):
    # Update the city model with weather data
    city.data = str(weather_data)
    city.tmp = tmp_sky(weather_data)
    # Update other fields as needed
    database.add(city)
    database.commit()
    return city


def tmp_sky(data):
    tmp = str(round(int(data["main"]["temp"])))
    sky = data["weather"][0]["main"]
    return f"{tmp}°C - {sky}"
