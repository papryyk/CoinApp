from django.views.generic import ListView

from .models import CallData

# Create your views here.


class StartingPage(ListView):
    template_name = "hub/index.html"
    model = CallData
    ordering = "market_cap_rank"
    context_object_name = "coins"
    ordering_dict = {
        "name": "name",
        "price": "price",
        "price_change_percentage_24h": "price_change_percentage_24h",
    }
