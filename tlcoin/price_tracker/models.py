from django.db import models

# List of coins
class Coins(models.Model):
    coin_id = models.CharField(max_length=50, unique=True)
    coin_name = models.CharField(max_length=50)

def __str__(self):
        return f'{self.coin_id}'

# coins price w.r.t time
class CoinPrices(models.Model):
    coin = models.ForeignKey(Coins, on_delete=models.RESTRICT)
    vs_currency = models.CharField(max_length=50, null=False)
    price = models.BigIntegerField(null=False)
    price_updated_at = models.DateTimeField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('coin_id', 'vs_currency', 'price', 'price_updated_at')

def __str__(self):
        return f'{self.coin_id}-{self.vs_currency}-{self.price}'