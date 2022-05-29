from datetime import datetime

from django import views
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .api.weather_wrapper import WEATHER_API_WRAPPER
from .models import *


class MainPageView(views.View):
    def get(self, request):
        """Weather api block"""
        weather_search = request.GET.get('weather_search', 'Minsk')
        weather_api_search_for_city = WEATHER_API_WRAPPER.get_weather_info_by_city(weather_search=weather_search)

        # Weather for current city
        city_temp = float('{:.3f}'.format((weather_api_search_for_city['main'].get('temp')) - 273.15))
        city_pressure = weather_api_search_for_city['main'].get('pressure')
        city_humidity = weather_api_search_for_city['main'].get('humidity')
        weather_description = weather_api_search_for_city['weather'][0].get('description')
        wind_speed = weather_api_search_for_city['wind'].get('speed')
        date_time = datetime.now().strftime('%d %b %Y | %I:%M:%S: %p')

        context = {
            'city_temp': city_temp,
            'city_pressure': city_pressure,
            'city_humidity': city_humidity,
            'weather_description': weather_description,
            'wind_speed': wind_speed,
            'date_time': date_time,
            'title': 'InfoOnePortal',
        }
        return render(request, 'index.html', context)
