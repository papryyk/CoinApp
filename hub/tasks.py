from workers import task
from django.utils import timezone
import requests

from .models import Coin


@task(schedule=40)
def api_to_db():
    api_url = "https://api.coingecko.com/api/v3/coins/markets?" \
              "vs_currency=usd&order=market_cap_desc&per_page=750&page=1"
    response = requests.get(api_url)
    results = response.json()
    print("I'm starting")

    for coin in results:

        db_coin = Coin.objects.filter(name=coin["name"])
        if db_coin:
            db_coin = Coin.objects.get(name=coin["name"])
            db_coin.current_price = coin["current_price"]
            db_coin.market_cap = coin["market_cap"]
            db_coin.price_change_percentage_24h = coin["price_change_percentage_24h"]
            db_coin.high_24h = coin["high_24h"]
            db_coin.low_24h = coin["low_24h"]
            db_coin.market_cap_rank = coin["market_cap_rank"]
            db_coin.image = coin["image"]
            db_coin.save()
            print(db_coin.name + " updated")
        else:
            db_coin = Coin()
            db_coin.name = coin["name"]
            db_coin.symbol = coin["symbol"]
            db_coin.current_price = coin["current_price"]
            db_coin.market_cap = coin["market_cap"]
            db_coin.price_change_percentage_24h = coin["price_change_percentage_24h"]
            db_coin.high_24h = coin["high_24h"]
            db_coin.low_24h = coin["low_24h"]
            db_coin.market_cap_rank = coin["market_cap_rank"]
            db_coin.upload_time = timezone.now()
            db_coin.save()
            print(db_coin.name + " added")

    for coin in Coin.objects.all():
        if coin.price_change_percentage_24h is None or coin.current_price == 0:
            coin.delete()
            print(coin.name + " deleted")

    print("Finished!")
