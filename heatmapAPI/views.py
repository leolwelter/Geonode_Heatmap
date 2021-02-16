from django.db.models import QuerySet
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from heatmapAPI.models import GeoNode
from heatmapAPI.serializers import GeoNodeSerializer
import logging

logger = logging.getLogger('django.server')


# define a custom filterset, which tells django-filter how to filter our queryset
class LookupFilterset(filters.FilterSet):
    lat_min = filters.filters.NumberFilter('latitude', lookup_expr='lte')
    lat_max = filters.filters.NumberFilter('latitude', lookup_expr='gte')
    long_min = filters.filters.NumberFilter('longitude', lookup_expr='lte')
    long_max = filters.filters.NumberFilter('longitude', lookup_expr='gte')

    class Meta:
        model = GeoNode
        fields = ['lat_min', 'lat_max', 'long_min', 'long_max']


class StandardPagination(LimitOffsetPagination):
    default_limit = 10000
    max_limit = 30000
    limit_query_param = 'limit'
    template = None


# be sure to set serializer_class and queryset
class GeoNodeViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = GeoNodeSerializer

    # queryset = GeoNode.objects.all()
    def get_queryset(self):
        qs = GeoNode.objects.all().order_by('id')
        logger.info('geonode queryset: {}'.format(qs.count()))
        return qs

    filter_backends = (filters.backends.DjangoFilterBackend,)
    filterset_class = LookupFilterset
    pagination_class = StandardPagination
