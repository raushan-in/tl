from __future__ import absolute_import, unicode_literals

import os

import requests
from celery import shared_task

COIN_SOURCE_URI = os.environ.get("COIN_SOURCE_URI", "https://api.coingecko.com/api/v3")

@shared_task
def refresh_price(coin="bitcoin", vs_currency="USD", seconds=40):
    '''
    Method to get coin price-vs-Currency periodic data from external data source
    '''
    response=requests.get(f"{COIN_SOURCE_URI}/simple/price?ids={coin}&vs_currencies={vs_currency}&include_last_updated_at=true")
    if response.status_code == 200:
        return response.json()
    else:
        print(f"status - {response.status_code}")
