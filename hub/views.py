from django.shortcuts import render
from django.views import View
from django.views.generic import ListView


from .models import CallData

# Create your views here.


class StartingPage(ListView):
    template_name = "hub/index.html"
    model = CallData
    ordering = "-current_price"
    context_object_name = "coins"



