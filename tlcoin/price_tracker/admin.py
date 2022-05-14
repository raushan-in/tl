from django.contrib import admin

from .models import CoinPrices, Coins

# Register your models here.
admin.site.register(Coins)

admin.site.register(CoinPrices)
