from rest_framework import serializers
from rates.models import Rate


class RateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rate
        fields = ['currency', 'rate', 'date']
