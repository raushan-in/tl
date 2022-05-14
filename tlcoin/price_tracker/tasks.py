from __future__ import absolute_import, unicode_literals

import os
from datetime import datetime

import pytz
import requests
from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import IntegrityError
from notification.tasks import notifier

from .models import CoinPrices, Coins

COIN_SOURCE_URI = os.environ.get("COIN_SOURCE_URI", "https://api.coingecko.com/api/v3")

@shared_task
def refresh_price(coin="bitcoin", vs_currency="USD"):
    '''
    Method to get coin price-vs-Currency periodic data from external data source
    '''
    try:
        coin_obj = Coins.objects.get(coin_id=coin)
    except ObjectDoesNotExist:
        print("Invalid Coin id")
        return

    response=requests.get(f"{COIN_SOURCE_URI}/simple/price?ids={coin}&vs_currencies={vs_currency}&include_last_updated_at=true")
    if response.status_code == 200:
        response_data = response.json()
        coin_deatil = response_data.get(coin)
        price = coin_deatil.get(vs_currency.lower())
        update_timestmap = coin_deatil.get("last_updated_at")

        if price and update_timestmap:
            price_updated_at = datetime.fromtimestamp(update_timestmap, tz=pytz.utc)

            try:
                coin_price = CoinPrices(coin=coin_obj, vs_currency=vs_currency, price=price, price_updated_at=price_updated_at)
                coin_price.save()
            except IntegrityError:
                print(f"no change in price of {coin}")
            else:
                notifier(price=price, coin=coin) # trigger notification task
        else:
            print("data missing in response")
    else:
        print(f"status - {response.status_code}")
