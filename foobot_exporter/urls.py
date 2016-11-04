from django.conf.urls import url, include
from django.contrib import admin

from rest_framework import routers
from .views import OwnerViewSet

router = routers.DefaultRouter()
router.register(r'owners', OwnerViewSet, base_name='owner')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls, namespace='api')),
]
