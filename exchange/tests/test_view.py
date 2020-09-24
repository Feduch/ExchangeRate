from django.test import TestCase
from http import HTTPStatus


class TestRate(TestCase):
    """ Test exchange for pair currencies """
    print("Test exchange for pair currencies")
    fixtures = ['currency.json', 'rates.json']

    def setUp(self):
        self.eur_czk = '/exchange/EUR/CZK/1.5/'
        self.czk_eur = '/exchange/CZK/EUR/1.5/'

    def test_eur_czk(self):
        response = self.client.get(self.eur_czk)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_czk_eur(self):
        response = self.client.get(self.czk_eur)
        self.assertEqual(response.status_code, HTTPStatus.OK)
