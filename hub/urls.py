from django.urls import path

from . import views

urlpatterns = [
    path("", views.StartingPage.as_view(), name="starting-page"),
]
