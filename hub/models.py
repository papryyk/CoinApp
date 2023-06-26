from django.db import models

# Create your models here.


class CallData(models.Model):
    name = models.TextField(null=True)
    symbol = models.TextField(null=True)
    current_price = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    upload_time = models.DateTimeField(null=True)
    market_cap = models.DecimalField(max_digits=50, decimal_places=10, null=True)
    price_change_percentage_24h = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    high_24h = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    low_24h = models.DecimalField(max_digits=20, decimal_places=10, null=True)
    market_cap_rank = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.name}"


class Ranges(models.Model):
    symbol = models.OneToOneField(CallData, on_delete=models.CASCADE, related_name="ranges")
    min_range = models.DecimalField(max_digits=20, decimal_places=10, default=1, null=True)
    max_range = models.DecimalField(max_digits=20, decimal_places=10, default=1, null=True)

    def __str__(self):
        return f"{self.symbol}"
