import decimal
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from currency.models import Currency


@api_view(['GET'])
def exchange(request, from_currency, to_currency, count):
    """
    Convert currency
    """
    from_currency_obj = Currency.objects.get(code__exact=from_currency)
    to_currency_obj = Currency.objects.get(code__exact=to_currency)

    rate_from = from_currency_obj.rates.latest('id').rate
    rate_to = to_currency_obj.rates.latest('id').rate

    if from_currency_obj.is_base:
        result = decimal.Decimal(count) * rate_to
    else:
        result = decimal.Decimal(count) * (rate_to / rate_from)

    return Response({'result': result}, status=status.HTTP_200_OK)