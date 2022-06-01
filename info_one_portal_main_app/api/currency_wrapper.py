import requests
from datetime import datetime
from decouple import config


class CurrencyApiWrapper:
    """Currency api"""
    # api used - https://apilayer.com/
    CURRENCY_USER_API_KEY = config('CURRENCY_USER_API_KEY')
    BASE_CURRENCY = config('BASE_CURRENCY')
    BASE_CURRENCIES = config('BASE_CURRENCIES')
    CURRENCY_API_URL = config('CURRENCY_API_URL')
    CURRENCIES_API_URL = config('CURRENCIES_API_URL')

    payload = {}
    headers = {
        'apikey': f'{CURRENCY_USER_API_KEY}'
    }

    # api request for many currencies
    def get_list_of_currencies(self):

        api_link_for_currency_rate = f'{self.CURRENCY_API_URL}' \
                                     f'?symbols={self.BASE_CURRENCIES}' \
                                     f'&base={self.BASE_CURRENCY}'

        api_link_currency_rate = requests.request(
            'GET', api_link_for_currency_rate, headers=self.headers, data=self.payload
        )
        api_data_currency_rate = api_link_currency_rate.json()
        return api_data_currency_rate

    # api request for currency converter
    def get_currency_rate_for_converter(self, currency_from='', currency_to='', currency_amount='', date_time=''):

        api_link_for_currencies_rate = f'{self.CURRENCIES_API_URL}' \
                                       f'?to={currency_to}' \
                                       f'&from={currency_from}' \
                                       f'&amount={currency_amount}' \
                                       f'&date={date_time}'

        api_link_currencies_rate = requests.request(
            'GET', api_link_for_currencies_rate, headers=self.headers, data=self.payload
        )
        api_data_currencies_rate = api_link_currencies_rate.json()
        return api_data_currencies_rate


CURRENCY_API_WRAPPER = CurrencyApiWrapper()
