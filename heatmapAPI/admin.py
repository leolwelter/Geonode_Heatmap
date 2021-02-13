from django.contrib import admin

# Register your models here.
from heatmapAPI.models import GeoNode

admin.site.register([GeoNode])
