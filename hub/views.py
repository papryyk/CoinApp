from django.views.generic import ListView
from django.views import View
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Coin, Ranges
from .forms import RangesForm

# Create your views here.


class StartingPage(ListView):
    template_name = "hub/index.html"
    model = Coin
    ordering = "market_cap_rank"
    context_object_name = "coins"


class CoinPage(View):
    def get(self, request, symbol):
        coin = get_object_or_404(Coin, symbol=symbol)
        context = {
            "name": coin.name,
            "symbol": coin.symbol,
            "current_price": coin.current_price,
            "image": coin.image,
            "ranges_form": RangesForm(instance=coin),
            }
        try:
            context["min_range"] = coin.ranges.min_range
            context["max_range"] = coin.ranges.max_range
        except Coin.ranges.RelatedObjectDoesNotExist:
            coin.ranges = Ranges()
            context["min_range"] = coin.ranges.min_range
            context["max_range"] = coin.ranges.max_range

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
            else:
                print("error")

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
            print("mam cie")

        return render(request, "hub/coin_details.html", context)

