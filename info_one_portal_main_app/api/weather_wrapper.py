import requests
from datetime import datetime
from decouple import config


class WeatherApiWrapper:
    """Weather api"""
    WEATHER_USER_API_KEY = config('WEATHER_USER_API_KEY')
    WEATHER_API_URL = config('WEATHER_API_URL')
    BASE_LOCATION_1 = config('BASE_LOCATION_1')
    BASE_LOCATION_2 = config('BASE_LOCATION_2')
    BASE_LOCATION_3 = config('BASE_LOCATION_3')
    BASE_LOCATION_4 = config('BASE_LOCATION_4')
    ALL_BASE_LOCATIONS = [BASE_LOCATION_1, BASE_LOCATION_2, BASE_LOCATION_3, BASE_LOCATION_4]

    # weather api request for searched city by user
    def get_weather_by_city_search(self, weather_search=''):

        api_link_for_city = f'{self.WEATHER_API_URL}?q={weather_search}&appid={self.WEATHER_USER_API_KEY}'
        api_link_city = requests.get(api_link_for_city)
        api_data_city = api_link_city.json()

        data_for_search_city = []

        if api_data_city['cod'] == '404':
            raise Exception('Incorrect city name, please check your city name and try again.')
        else:
            data_search_city = {
                'city_temp': float('{:.3f}'.format((api_data_city['main'].get('temp')) - 273.15)),
                'city_pressure': api_data_city['main'].get('pressure'),
                'city_humidity': api_data_city['main'].get('humidity'),
                'weather_description': api_data_city['weather'][0].get('description'),
                'wind_speed': api_data_city['wind'].get('speed'),
                'date_time': datetime.now().strftime('%d %b %Y | %I:%M:%S: %p')
            }
            data_for_search_city.append(data_search_city)
        return data_for_search_city

    # weather api request for base 4 cities for main_page.html
    def get_weather_for_bases_cities(self):

        all_weather_data = []

        # add weather information to each city to one variable
        for location in self.ALL_BASE_LOCATIONS:
            api_link_for_base_locations = f'{self.WEATHER_API_URL}?q={location}&appid={self.WEATHER_USER_API_KEY}'
            api_link_base_locations = requests.get(api_link_for_base_locations)
            api_data_base_locations = api_link_base_locations.json()
            if api_data_base_locations['cod'] == '404':
                raise Exception('Incorrect city name, please check your city name and try again.')
            else:
                if location == self.ALL_BASE_LOCATIONS[0]:
                    all_weather_data.append(api_data_base_locations)
                elif location == self.ALL_BASE_LOCATIONS[1]:
                    all_weather_data.append(api_data_base_locations)
                elif location == self.ALL_BASE_LOCATIONS[2]:
                    all_weather_data.append(api_data_base_locations)
                elif location == self.ALL_BASE_LOCATIONS[3]:
                    all_weather_data.append(api_data_base_locations)

        weather_data = []

        # convert data to readable format
        for item in all_weather_data:
            weather = {
                'city_name': item.get('name'),
                'city_temp': float('{:.3f}'.format((item['main'].get('temp')) - 273.15)),
                'city_pressure': item['main'].get('pressure'),
                'city_humidity': item['main'].get('humidity'),
                'weather_description': item['weather'][0].get('description'),
                'wind_speed': item['wind'].get('speed'),
                'date_time': datetime.now().strftime('%d %b %Y | %I:%M:%S: %p')
            }
            weather_data.append(weather)
        return weather_data


WEATHER_API_WRAPPER = WeatherApiWrapper()
