from rest_framework import authentication
from users.models import Ggjyu
from .serializers import GgjyuSerializer
from rest_framework import viewsets


class GgjyuViewSet(viewsets.ModelViewSet):
    serializer_class = GgjyuSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Ggjyu.objects.all()
