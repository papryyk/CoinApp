from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Coin(models.Model):
    name = models.TextField(null=True)
    symbol = models.TextField(null=True)
    current_price = models.DecimalField(
        max_digits=20, decimal_places=10, null=True)
    history_price = models.TextField(null=True)
    upload_time = models.TextField(null=True)
    private_history_price = models.TextField(null=True)
    private_upload_time = models.TextField(null=True)
    market_cap = models.DecimalField(
        max_digits=50, decimal_places=10, null=True)
    price_change_percentage_24h = models.DecimalField(
        max_digits=20, decimal_places=10, null=True)
    high_24h = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    low_24h = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    market_cap_rank = models.IntegerField(null=True)
    image = models.URLField(null=True)
    cg_identifier = models.TextField(null=True)

    def __str__(self):
        return f"{self.name}"
    


class Ranges(models.Model):
    coin = models.ForeignKey(
        Coin, on_delete=models.PROTECT, related_name="ranges", null=True)
    min_range = models.DecimalField(
        max_digits=20, decimal_places=10, null=True)
    max_range = models.DecimalField(
        max_digits=20, decimal_places=10, null=True)
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="ranges", null=True)

    def __str__(self):
        return f"{self.coin}"
    
