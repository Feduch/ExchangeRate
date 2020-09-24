from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import permissions
from rates.serializers import RateSerializer
from rates.models import Rate


class RateViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows rate to be viewed.
    """
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['GET'])
def date_updated(request):
    """
    Return last date updated currency rate
    """
    return Response({'date': Rate.objects.latest('id').date}, status=status.HTTP_200_OK)