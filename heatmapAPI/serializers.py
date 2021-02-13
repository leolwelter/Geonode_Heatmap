import rest_framework.serializers as serializers

#     geoname_id = models.IntegerField(primary_key=True)
#     registered_country_geoname_id = models.IntegerField
#     latitude = models.IntegerField
#     longitude = models.IntegerField
from heatmapAPI.models import GeoNode


class GeoNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoNode
        fields = ('id', 'geoname_id', 'latitude', 'longitude')
