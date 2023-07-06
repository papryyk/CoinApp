from django.views.generic import ListView
from django.views import View
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import CallData

# Create your views here.


class StartingPage(ListView):
    template_name = "hub/index.html"
    model = CallData
    ordering = "market_cap_rank"
    context_object_name = "coins"


class CoinPage(View):
    def get(self, request, symbol):
        coin = get_object_or_404(CallData, symbol=symbol)
        context = {
            "name": coin.name,
            "symbol": coin.symbol,
            "current_price": coin.current_price,
            }
        try:
            context["min_range"] = coin.ranges.min_range
            context["max_range"] = coin.ranges.max_range
        except CallData.ranges.RelatedObjectDoesNotExist:
            pass

        return render(request, "hub/coin_details.html", context)
