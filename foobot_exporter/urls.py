from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView

from rest_framework import routers
from .views import OwnerViewSet, DeviceViewSet

router = routers.DefaultRouter()
router.register(r'owners', OwnerViewSet, base_name='owner')
router.register(r'devices', DeviceViewSet, base_name='device')

urlpatterns = [
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^$', RedirectView.as_view(url='/')),
]
