from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from .models import Coin, Ranges
from .forms import RangesForm, UserRegisterForm, signInForm

# Create your views here.


def delete_range(request, symbol):
    coin = Coin.objects.get(symbol=symbol)
    Ranges.objects.get(coin=coin).delete()

    return HttpResponseRedirect(reverse("coin-details", args=[symbol]))


class StartingPage(View):

    def get(self, request):
        form = signInForm()
        context = {
            "coins": Coin.objects.all(),
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
                # Redirect to a success page or do whatever is needed
                print("logged in")
                return HttpResponseRedirect(reverse("starting-page"))
            else:
                # Handle invalid login
                form.add_error(None, 'Invalid login credentials')
                print("not logged, error")

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


class SignUpView(FormView):
    template_name = 'hub/register.html'
    form_class = UserRegisterForm
    success_url = "register/thanks"

    def form_valid(self, form):
        form.save()
        return super(SignUpView, self).form_valid(form)


class RegisterThansk(View):
    def get(self, request):
        return render(request, "hub/register_thanks.html")
