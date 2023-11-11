from django.db import models

# Create your models here.


class Coin(models.Model):
    name = models.TextField(null=True)
    symbol = models.TextField(null=True)
    current_price = models.DecimalField(
        max_digits=20, decimal_places=10, null=True)
    history_price = models.TextField(null=True)
    upload_time = models.TextField(null=True)
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
    coin = models.OneToOneField(
        Coin, on_delete=models.CASCADE, related_name="ranges")
    min_range = models.DecimalField(
        max_digits=20, decimal_places=10, null=True)
    max_range = models.DecimalField(
        max_digits=20, decimal_places=10, null=True)

    def __str__(self):
        return f"{self.coin}"


class User(models.Model):
    username: models.CharField(max_length=20)
    email: models.EmailField((""), max_length=254)
    first_name: models.CharField(max_length=20, null=True)
    last_name: models.CharField(max_length=20, null=True)
