import httpx
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('OPENWEATHER_KEY')
URL_LOCATION = "http://api.openweathermap.org/geo/1.0/direct"
URL_WEATHER = "https://api.openweathermap.org/data/2.5/weather"

def get_location_coordinates(city: str, state: str, country: str):
    params = {'q': [city, state, country], 'appid': API_KEY}
    response = httpx.get(URL_LOCATION, params=params)
    geo_dict = response.json()
    geo_dict = geo_dict[0]
    latitude = geo_dict.get('lat')
    longitude = geo_dict.get('lon')

    return latitude, longitude

def get_weather():
    city = input("Enter your city name: ")
    state = input("Enter your state abbreviation(If no state, hit enter): ")
    country = input("Enter your country code: ")
    unit_input = input("Specify temperature unit, C or F: ").upper()
    units = "imperial" if unit_input == "F" else "metric"

    latitude, longitude = get_location_coordinates(city, state, country)

    params = {'lat': latitude, 'lon': longitude, 'units': units, 'appid': API_KEY}
    response = httpx.get(URL_WEATHER, params=params)
    wx_dict = response.json()
    wx_name = wx_dict.get('name')
    wx_main = wx_dict.get('main')
    wx_wx_list = wx_dict.get('weather')
    wx_wx_dict = wx_wx_list[0]

    print(
        f"There currently is {wx_wx_dict.get('description')} in {wx_name}. The current temperature is {int(round(wx_main.get('temp')))}{unit_input} and it feels like {int(round(wx_main.get('feels_like')))}{unit_input}."
    )


get_weather()