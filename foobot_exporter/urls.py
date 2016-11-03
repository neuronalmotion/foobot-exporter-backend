from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from .views import DeviceViewSet

router = routers.DefaultRouter()
router.register(r'devices', DeviceViewSet, base_name='devices')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
