from rest_framework import serializers
from currency.models import Currency


class CurrencySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Currency
        fields = ['name', 'code', 'is_base']
