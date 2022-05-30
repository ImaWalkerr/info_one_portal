from django import views
from django.shortcuts import render, redirect

from .api.weather_wrapper import WEATHER_API_WRAPPER
from .models import *


class MainPageView(views.View):

    def get(self, request):
        """Weather api block"""
        # Weather for searched city
        weather_search = request.GET.get('weather_search', 'Minsk')
        weather_api_search_for_city = WEATHER_API_WRAPPER.get_weather_by_city_search(weather_search=weather_search)

        # Weather for base 4 cities
        weather_api_base_locations = WEATHER_API_WRAPPER.get_weather_for_bases_cities()
        weather_for_base_location_1 = weather_api_base_locations[0]
        weather_for_base_location_2 = weather_api_base_locations[1]
        weather_for_base_location_3 = weather_api_base_locations[2]
        weather_for_base_location_4 = weather_api_base_locations[3]

        context = {
            'weather_api_search_for_city': weather_api_search_for_city,
            'weather_for_base_location_1': weather_for_base_location_1,
            'weather_for_base_location_2': weather_for_base_location_2,
            'weather_for_base_location_3': weather_for_base_location_3,
            'weather_for_base_location_4': weather_for_base_location_4,
            'title': 'InfoOnePortal',
        }
        return render(request, 'index.html', context)
