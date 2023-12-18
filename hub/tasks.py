from workers.worker import task

from time import sleep
import datetime

from django.utils import timezone, dateformat
import requests

from .models import Coin


@task()
def api_to_db():

    # Get chart data
    db_coins = Coin.objects.all()
    for coin_chart in db_coins:
        coin_id = coin_chart.cg_identifier
        if coin_id == None:
            print(f"{coin_id} - loop wasted")
            sleep(35)
        else:
            print(
                f"{dateformat.format(timezone.now(),'Y-m-d H:i:s')} Updating the chart for {coin_id}")
            api_url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart?vs_currency=usd&days=365"
            response = requests.get(api_url)
            results = response.json()
            for result in results["prices"]:

                coin_chart.upload_time += f"{datetime.datetime.utcfromtimestamp(int(result[0])/1000).strftime('%Y-%m-%d %H:%M:%S')},"
                coin_chart.history_price += f"{result[1]},"
                coin_chart.save()
            sleep(35)
        # Get current coin price
        api_url = "https://api.coingecko.com/api/v3/coins/markets?" \
            "vs_currency=usd&order=market_cap_desc&per_page=250&page=1"
        response = requests.get(api_url)
        results = response.json()
        print(
            f"{dateformat.format(timezone.now(),'Y-m-d H:i:s')} Retrieving current prices")
        for coin in results:

            db_coin = Coin.objects.filter(name=coin["name"])
            if db_coin:
                db_coin = Coin.objects.get(name=coin["name"])
                db_coin.current_price = coin["current_price"]
                # db_coin.private_history_price = ""
                # db_coin.private_upload_time = ""
                db_coin.private_history_price += f"{coin['current_price']},"
                db_coin.private_upload_time += f"{dateformat.format(timezone.now(),'Y-m-d H:i:s')},"
                db_coin.market_cap = coin["market_cap"]
                db_coin.price_change_percentage_24h = coin["price_change_percentage_24h"]
                db_coin.high_24h = coin["high_24h"]
                db_coin.low_24h = coin["low_24h"]
                db_coin.market_cap_rank = coin["market_cap_rank"]
                db_coin.image = coin["image"]
                db_coin.cg_identifier = coin["id"]
                db_coin.save()
            else:
                db_coin = Coin()
                db_coin.name = coin["name"]
                db_coin.symbol = coin["symbol"]
                db_coin.current_price = coin["current_price"]
                # db_coin.private_history_price = ""
                # db_coin.private_upload_time = ""
                db_coin.private_history_price = f"{dateformat.format(timezone.now(),'Y-m-d H:i:s')},"
                db_coin.private_upload_time = f"{coin['current_price']},"
                db_coin.market_cap = coin["market_cap"]
                db_coin.price_change_percentage_24h = coin["price_change_percentage_24h"]
                db_coin.high_24h = coin["high_24h"]
                db_coin.low_24h = coin["low_24h"]
                db_coin.market_cap_rank = coin["market_cap_rank"]
                db_coin.cg_identifier = coin["id"]
                db_coin.save()

        for coin in Coin.objects.all():
            if coin.price_change_percentage_24h is None or coin.current_price == 0:
                coin.delete()
                print(coin.name + " deleted")

        sleep(35)
