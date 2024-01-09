from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from .models import Coin, Ranges, User
from .forms import RangesForm, UserRegisterForm, signInForm

# Create your views here.


def delete_range(request, symbol):
    coin = Coin.objects.get(symbol=symbol)
    Ranges.objects.get(coin=coin, user=request.user).delete()

    return HttpResponseRedirect(reverse("coin-details", args=[symbol]))


def logout_button(request):
    logout(request)

    return HttpResponseRedirect(reverse("starting-page"))


class StartingPage(View):

    def get(self, request):
        form = signInForm()
        context = {
            "coins": Coin.objects.all().order_by("market_cap_rank"),
            "user": request.user,
            "form": form
        }

        return render(request, "hub/index.html", context)

    def post(self, request):
        form = signInForm(request.POST)
        context = {
            "coins": Coin.objects.all(),
            "form": form
        }

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                context['user'] = user
                return HttpResponseRedirect(reverse("starting-page"))
            else:
                form.add_error(None, 'Invalid login credentials')

        return render(request, "hub/index.html", context)

# TODO Setting ranges can be allowed only for logged in users
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
        }
        if request.user.is_authenticated:
            try:
                range = Ranges.objects.get(coin__symbol=symbol, user=request.user)
                context["min_range"] = range.min_range
                context["max_range"] = range.max_range
            except Ranges.DoesNotExist:
                # Range is not set
                pass

        return render(request, "hub/coin_details.html", context)

    def post(self, request, symbol):
        coin = Coin.objects.get(symbol=symbol)
        if request.user.is_authenticated:
            range = Ranges.objects.filter(coin__symbol=symbol, user=request.user)
            if range:
                range = Ranges.objects.get(coin__symbol=symbol, user=request.user)
                form = RangesForm(request.POST, instance=range)
                print("if range")
                if form.is_valid():
                    print("if range, form.save()")
                    form.save()
            else:
                print("no range found")
                form = RangesForm(request.POST, initial={'user': request.user})
                if form.is_valid():
                    coin_range = form.save(commit=False)
                    coin_range.coin = coin
                    coin_range.user = request.user
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
                context["min_range"] = range.min_range
                context["max_range"] = range.max_range
            except Ranges.DoesNotExist:
                # Range not set
                pass

            return render(request, "hub/coin_details.html", context)
        else:
            context = {
                "name": coin.name,
                "symbol": coin.symbol,
                "current_price": coin.current_price,
                "image": coin.image,
                "ranges_form": RangesForm(request.POST),
                "min_range": "You have to be logged in to do that",
                "max_range": "You have to be logged in to do that"
                }
            return render(request, "hub/coin_details.html", context)


class SignUpView(View):
    def get(self, request):
        form = signInForm()
        form2 = UserRegisterForm()
        context = {
            "form": form,
            "form2": form2
        }

        return render(request, "hub/register.html", context)

    def post(self, request):
        form = signInForm()
        form2 = UserRegisterForm(request.POST)
        context = {
            "form": form,
            "form2": form2
        }

        if form2.is_valid():
            form2.save()
            return HttpResponseRedirect(reverse("starting-page"))
        else:
            print(form2.errors)
            return render(request, "hub/register.html", context)


class MyProfileView(View):
    def get(self, request, user):
        context = {
            "current_user": request.user,
            "coins": Coin.objects.all()[:10]
        }

        return render(request, "hub/account.html", context)
