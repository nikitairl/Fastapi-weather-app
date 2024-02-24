from dataclasses import dataclass

import requests
from sqlalchemy.orm import Session

from . import main

URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"

lat = 0
lon = 0
API_key = "729b98baef5347afc700bc1ba8077b5d"

url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}"
request_data = requests.get(url)

data = request_data.json()
print(data)