
from price_tracker.models import CoinPrices
from rest_framework import serializers


class CoinPriceSerializer(serializers.ModelSerializer):
    coin = serializers.CharField(source='coin.coin_name')
    timestamp = serializers.CharField(source='price_updated_at')

    class Meta:
        model = CoinPrices
        fields = ['timestamp', 'price', 'coin']
