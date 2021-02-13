from django.urls import path, include
from rest_framework import routers

from heatmapAPI.views import GeoNodeViewset

router = routers.DefaultRouter()
router.register(r'geonode', GeoNodeViewset, basename='GeoNode')

urlpatterns = [
    path('', include(router.urls)),
]
