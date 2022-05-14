from django.db import models

# List of coins
class PriceThresholdNotifications(models.Model):
    email = models.EmailField()
    lower_threshold_flag = models.BooleanField()
    upper_threshold_flag = models.BooleanField()
    coin_id = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "price notifications"

    def __str__(self):
            return f'{self.email} - {self.created_at}'