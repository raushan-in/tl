from django.db import models

# List of coins
class Coins(models.Model):
    coin_id = models.CharField(max_length=50, unique=True)
    coin_name = models.CharField(max_length=50)

def __str__(self):
        return f'{self.coin_id}'