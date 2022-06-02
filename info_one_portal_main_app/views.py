from django import views
from django.shortcuts import render, redirect

from .api.currency_wrapper import CURRENCY_API_WRAPPER
from .api.weather_wrapper import WEATHER_API_WRAPPER
from .models import *


class MainPageView(views.View):

    def get(self, request):
        # Weather api block
        # Weather for searched city
        weather_search = request.GET.get('weather_search', 'Minsk')
        weather_api_search_for_city = WEATHER_API_WRAPPER.get_weather_by_city_search(weather_search=weather_search)
        weather_for_searched_city = weather_api_search_for_city[0]

        # Weather for base 4 cities
        weather_api_base_locations = WEATHER_API_WRAPPER.get_weather_for_bases_cities()
        weather_for_base_location_1 = weather_api_base_locations[0]
        weather_for_base_location_2 = weather_api_base_locations[1]
        weather_for_base_location_3 = weather_api_base_locations[2]
        weather_for_base_location_4 = weather_api_base_locations[3]

        # Currency api block
        # Base currencies rates
        # currencies = CURRENCY_API_WRAPPER.get_list_of_currencies()

        # Currency rate for user
        currency_from = request.GET.get('currency-from')
        currency_to = request.GET.get('currency-to')
        currency_amount = request.GET.get('currency-amount')
        date_time = request.GET.get('date')
        # currency_rate_for_user = CURRENCY_API_WRAPPER.get_currency_rate_for_converter(
        #     currency_from=currency_from, currency_to=currency_to, currency_amount=currency_amount, date_time=date_time
        # )

        context = {
            'weather_for_searched_city': weather_for_searched_city,
            'weather_for_base_location_1': weather_for_base_location_1,
            'weather_for_base_location_2': weather_for_base_location_2,
            'weather_for_base_location_3': weather_for_base_location_3,
            'weather_for_base_location_4': weather_for_base_location_4,
            # 'currencies': currencies,
            # 'currency_rate_for_user': currency_rate_for_user,
            'title': 'InfoOnePortal',
        }
        return render(request, 'index.html', context)
