from django.views import View
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Coin, Ranges
from .forms import RangesForm

# Create your views here.


def delete_range(request, symbol):
    coin = Coin.objects.get(symbol=symbol)
    Ranges.objects.get(coin=coin).delete()

    return HttpResponseRedirect(reverse("coin-details", args=[symbol]))


class StartingPage(View):

    def get(self, request):
        sort_buttons = {"price_sort": "current_price",
                        "h_sort": "price_change_percentage_24h",
                        "low_h_sort": "low_24h",
                        "high_h_sort": "high_24h",
                        "mcap_sort": "market_cap",
                        "coin_sort": "symbol",
                        "rank_sort": "market_cap_rank",
                        "min_sort": "ranges",
                        "max_sort": "ranges",
                        }

        context = {}

        for s_button in sort_buttons:
            s_button_value = request.GET.get(s_button)
            if s_button_value is not None:
                if s_button_value == "TRUE":
                    price_boo = True
                else:
                    price_boo = False

                if price_boo:
                    sort_sign = ""
                else:
                    sort_sign = "-"

                context["coins"] = Coin.objects.all().order_by(f"{sort_sign}{sort_buttons[s_button]}")
                context["price_boo"] = price_boo
                break
            else:
                context["coins"] = Coin.objects.all()

        context["coins_ranges"] = Coin.objects.all()
        context["high_price"] = Coin.objects.all().order_by("-current_price")[0:3]
        context["lowest_change"] = Coin.objects.all().order_by("price_change_percentage_24h")[0:3]
        context["highest_change"] = Coin.objects.all().order_by("-price_change_percentage_24h")[0:3]
        context["highest_mcap"] = Coin.objects.all().order_by("-market_cap")[0:3]

        return render(request, "hub/index.html", context)

    def post(self, request):

        context = {
            "coins": Coin.objects.all().order_by("current_price"),
            "high_price": Coin.objects.all().order_by("-current_price")[0:3],
            "lowest_change": Coin.objects.all().order_by("price_change_percentage_24h")[0:3],
            "highest_change": Coin.objects.all().order_by("-price_change_percentage_24h")[0:3],
            "highest_mcap": Coin.objects.all().order_by("-market_cap")[0:3],
        }

        return render(request, "hub/index.html", context)

class CoinPage(View):
    def get(self, request, symbol):
        coin = get_object_or_404(Coin, symbol=symbol)
        context = {
            "name": coin.name,
            "symbol": coin.symbol,
            "current_price": coin.current_price,
            "image": coin.image,
            "ranges_form": RangesForm(instance=coin),
            "coin": coin,
            "range_exists": Ranges.objects.filter(coin=coin)
            }
        try:
            context["min_range"] = coin.ranges.min_range
            context["max_range"] = coin.ranges.max_range
        except Coin.ranges.RelatedObjectDoesNotExist:
            # coin.ranges = Ranges()
            # context["min_range"] = coin.ranges.min_range
            # context["max_range"] = coin.ranges.max_range
            pass

        return render(request, "hub/coin_details.html", context)

    def post(self, request, symbol):
        coin = Coin.objects.get(symbol=symbol)
        try:
            form = RangesForm(request.POST, instance=coin.ranges)
            if form.is_valid():
                form.save()
            else:
                print("error")

                return HttpResponseRedirect(reverse("coin-details", args=[symbol]))

        except Coin.ranges.RelatedObjectDoesNotExist:
            form = RangesForm(request.POST)
            if form.is_valid():
                coin_range = form.save(commit=False)
                coin_range.coin = coin
                coin_range.save()

                return HttpResponseRedirect(reverse("coin-details", args=[symbol]))

        context = {
            "name": coin.name,
            "symbol": coin.symbol,
            "current_price": coin.current_price,
            "image": coin.image,
            "ranges_form": form
        }
        try:
            context["min_range"] = coin.ranges.min_range
            context["max_range"] = coin.ranges.max_range
        except Coin.ranges.RelatedObjectDoesNotExist:
            pass

        return render(request, "hub/coin_details.html", context)
