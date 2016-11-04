from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import detail_route

from .serializers import DeviceSerializer
from .models import Device
from . import foobot_service

class SecretKeyMixin(object):
    def get_secret_key_from_request(self, request):
        secret_key = request.META.get('HTTP_X_API_KEY_TOKEN')
        response = None
        if not secret_key:
            response = Response('Missing API key', status=status.HTTP_401_UNAUTHORIZED)
        return (secret_key, response)


class OwnerViewSet(viewsets.ViewSet):
    queryset = None
    serializer_class = None
    lookup_url_kwarg = 'username'
    lookup_value_regex = '[^/]+'

    @detail_route(methods=['get'], url_path='devices')
    def get_devices(self, request, username=None):
        secret_key, response = self.get_secret_key_from_request(request)
        if not secret_key:
            return response

        devices, status_code = foobot_service.get_devices(username, secret_key)
        return Response(devices, status=status_code)

class DeviceViewSet(viewsets.ViewSet, SecretKeyMixin):
    queryset = None
    serializer_class = None
    lookup_url_kwarg = 'uuid'

    @detail_route(methods=['get'], url_path='datapoints/(?P<period>\d+)/last/(?P<average_by>\d+)')
    def get_datapoints(self, request, uuid=None, period=None, average_by=None):
        secret_key, response = self.get_secret_key_from_request(request)
        if not secret_key:
            return response

        datapoints, status_code = foobot_service.get_datapoints_last(
                secret_key,
                uuid,
                period,
                average_by)
        return Response(datapoints, status=status_code)

