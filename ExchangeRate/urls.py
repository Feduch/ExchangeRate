from django.contrib import admin
from django.urls import path, include, register_converter
from rest_framework import routers
from ExchangeRate.converts import FloatUrlParameterConverter
from currency.views import CurrencyViewSet
from rates.views import RateViewSet, date_updated
from exchange.views import exchange

register_converter(FloatUrlParameterConverter, 'float')

router = routers.DefaultRouter()
router.register(r'currency', CurrencyViewSet)
router.register(r'rate', RateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('exchange/<str:from_currency>/<str:to_currency>/<float:count>/', exchange),
    path('date/updated/', date_updated),
    path('admin/', admin.site.urls),
]
