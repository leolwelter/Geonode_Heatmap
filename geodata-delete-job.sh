#!/bin/bash

# This runs a simple command to drop all data in the heatmapAPI_geonode table
# required because Dask does not have functionality to do this currently
psql -c "DELETE FROM \"heatmapAPI_geonode\"" -d geodata -U geodatauser -a -o ~/geodata-delete-job.log
