import requests
from datetime import datetime
from decouple import config


class WeatherApiWrapper:
    """Weather api"""
    def get_weather_info_by_city(self, weather_search=''):

        user_api_key = config('WEATHER_KEY')
        location = weather_search

        api_link_for_city = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={user_api_key}'
        api_link_city = requests.get(api_link_for_city)
        api_data_city = api_link_city.json()

        if api_data_city['cod'] == '404':
            print('Invalid city: {}, please check your city name and try again'.format(location))
        else:
            return api_data_city


WEATHER_API_WRAPPER = WeatherApiWrapper()
