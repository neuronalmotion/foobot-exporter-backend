from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import DeviceSerializer
from .models import Device
from . import foobot_service

class DeviceViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer

    def get_queryset(self):
        return None

    def list(self, request):
        devices = foobot_service.get_devices('', '')
        return Response(devices)

