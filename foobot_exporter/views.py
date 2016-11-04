from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from .serializers import DeviceSerializer
from .models import Device
from . import foobot_service

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = None
    serializer_class = None
    lookup_url_kwarg = 'username'
    lookup_value_regex = '[^/]+'

    @detail_route(methods=['get'], url_path='devices')
    def get_devices(self, request, username=None):
        secretKey = request.META.get('HTTP_X_API_KEY_TOKEN')

        if not secretKey:
            return Response('Missing API key', status=status.HTTP_401_UNAUTHORIZED)

        devices = foobot_service.get_devices(username, secretKey)
        return Response(devices)

