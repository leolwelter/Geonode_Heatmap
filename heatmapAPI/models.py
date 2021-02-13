from django.db import models


class GeoNode(models.Model):
    geoname_id = models.IntegerField(default=None)
    registered_country_geoname_id = models.IntegerField(default=None)
    latitude = models.FloatField(default=None)
    longitude = models.FloatField(default=None)
