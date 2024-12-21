from dotenv import load_dotenv
import os
import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
load_dotenv()
API_KEY = os.getenv("API_KEY")

CITY = "London"
url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

def kelvin_to_celcius_fahrenheit(kelvin):
    celcius = kelvin - 273.15
    fahrenheit = celcius * (9/5) + 32
    return celcius, fahrenheit


response = requests.get(url).json()
temp_kelvin = response['main']['temp']
temp_celcius, temp_fahrenheit = kelvin_to_celcius_fahrenheit(temp_kelvin)
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'])


print(temp_fahrenheit)
print("Sunrise time:" + str(sunrise_time))