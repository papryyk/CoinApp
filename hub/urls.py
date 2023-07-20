from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPage.as_view(), name="starting-page"),
    path("<symbol>", views.CoinPage.as_view(), name="coin-details"),
    path("delete_range/<symbol>", views.delete_range, name="delete-range")
]
