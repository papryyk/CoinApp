from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPage.as_view(), name="starting-page"),
    path("coin/<symbol>", views.CoinPage.as_view(), name="coin-details"),
    path("delete_range/<symbol>", views.delete_range, name="delete-range"),
    path("register", views.SignUpView.as_view(), name="register-page"),
    path("logout", views.logout_button, name="logout-button")
]
