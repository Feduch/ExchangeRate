from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from http import HTTPStatus
from rates import views


class TestRate(APITestCase):
    """ Test ViewSet for Rate """
    print("Test ViewSet for Rate")
    fixtures = ['currency.json', 'rates.json']

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.RateViewSet.as_view({'get': 'list'})
        self.rate_uri = '/rate/'
        self.date_updated_uri = '/date/updated/'

    def test_list(self):
        request = self.factory.get(self.rate_uri)
        response = self.view(request)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_list2(self):
        response = self.client.get(self.rate_uri)
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_date_updated(self):
        response = self.client.get(self.date_updated_uri)
        self.assertEqual(response.status_code, HTTPStatus.OK)
