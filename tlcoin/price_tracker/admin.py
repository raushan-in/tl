from django.contrib import admin
from .models import Coins, CoinPrices

# Register your models here.
admin.site.register(Coins)

admin.site.register(CoinPrices)
