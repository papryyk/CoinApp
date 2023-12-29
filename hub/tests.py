from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone, dateformat

from .models import Coin, Ranges

# Create your tests here.

class hubTests(TestCase):

    #Create account, login, view index page
    def test_views(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('starting-page'))
        self.assertEqual(response.status_code, 200)

    #Create & display coin
    def test_coin(self):
        coin = Coin(name="test", symbol="TEST", current_price=1, private_history_price="1", 
                    private_upload_time=f"{dateformat.format(timezone.now(),'Y-m-d H:i:s')},", market_cap=1, price_change_percentage_24h=1.0,
                     high_24h=1, low_24h=1, market_cap_rank=1, cg_identifier="test" )
        coin.save()
        response = self.client.get(reverse('starting-page'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test')

    #Create & display coin ranges
    def test_range(self):
        coin = Coin(name="test", symbol="TEST", current_price=1, private_history_price="1", 
                    private_upload_time=f"{dateformat.format(timezone.now(),'Y-m-d H:i:s')},", market_cap=1, price_change_percentage_24h=1.0,
                     high_24h=1, low_24h=1, market_cap_rank=1, cg_identifier="test" )
        coin.save()
        coin_range = Ranges(coin=coin, min_range=10, max_range=100)
        coin_range.save()
        response = self.client.get(reverse('starting-page'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test')
        self.assertContains(response, '10')
        self.assertContains(response, '100')