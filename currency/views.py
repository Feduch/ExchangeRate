from rest_framework import viewsets
from rest_framework import permissions
from currency.serializers import CurrencySerializer
from currency.models import Currency


class CurrencyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows currency to be viewed or edited.
    """
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [permissions.AllowAny]
