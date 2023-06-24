from workers import task
from django.utils import timezone
import requests

from .models import CallData


@task(schedule=40)
def api_to_db():
    api_url = "https://api.coingecko.com/api/v3/coins/markets?" \
              "vs_currency=usd&order=market_cap_desc&per_page=250&page=1"
    response = requests.get(api_url)
    results = response.json()

    for coin in results:

        db_coin = CallData.objects.filter(name=coin["name"])
        if db_coin:
            db_coin = CallData.objects.get(name=coin["name"])
            db_coin.current_price = coin["current_price"]
            db_coin.upload_time = timezone.now()
            db_coin.save()
            print("Database updated!")
        else:
            db_coin = CallData()
            db_coin.name = coin["name"]
            db_coin.symbol = coin["symbol"]
            db_coin.current_price = coin["current_price"]
            db_coin.upload_time = timezone.now()
            db_coin.save()
            print("New record in database!")

