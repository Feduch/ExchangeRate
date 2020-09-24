from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from currency import views


class TestCurrency(APITestCase):
    """ Test ViewSet for Currency """
    print("est ViewSet for Currency")

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.CurrencyViewSet.as_view({'get': 'list'})
        self.uri = '/currency/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))

    def test_list2(self):
        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))
