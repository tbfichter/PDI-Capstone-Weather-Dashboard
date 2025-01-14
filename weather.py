import httpx

API_KEY = ""

def get_location_coordinates(city: str, state: str, country: str):
    params = {'q': [city, state, country], 'appid': API_KEY}
    geo = httpx.get('http://api.openweathermap.org/geo/1.0/direct', params=params)
    geo_dict = geo.json()
    geo_dict = geo_dict[0]
    latitude = geo_dict.get('lat')
    longitude = geo_dict.get('lon')

    return latitude, longitude

def get_weather():
    city = str(input("Enter your city name:"))
    state = str(input("Enter your state abbreviation:"))
    country = str(input("Enter your country code:"))
    units = str(input("Specify units or measurement, metric(Celsuis) or imperial(fahrenheit):"))
    latitude, longitude = get_location_coordinates(city, state, country)

    params = {'lat': latitude, 'lon': longitude, 'units': units, 'appid': API_KEY}
    weather = httpx.get('https://api.openweathermap.org/data/2.5/weather', params=params)
    wx_dict = weather.json()
    wx_name = wx_dict.get('name')
    wx_main = wx_dict.get('main')
    wx_wx = wx_dict.get('weather')
    wx_wx = wx_wx[0]


    print(f"There currently is {wx_wx.get('description')} in {wx_name}. The current temperature is {wx_main.get('temp')} and it feels like {wx_main.get('feels_like')}.")






get_weather()