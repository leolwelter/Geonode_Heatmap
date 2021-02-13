import sys

import dask.dataframe as dd
from dask.diagnostics import progress
import numpy as np

if __name__ == '__main__':
    columns = ['network', 'geoname_id', 'registered_country_geoname_id', 'represented_country_geoname_id',
               'is_anonymous_proxy',
               'is_satellite_provider', 'postal_code', 'latitude', 'longitude', 'accuracy_radius']

    types = {'geoname_id': np.int32,
             'registered_country_geoname_id': np.int32,
             'latitude': np.float16,
             'longitude': np.float16}
    used_cols = ['geoname_id', 'latitude', 'longitude', 'registered_country_geoname_id']
    df = dd.read_csv('data/GeoLite2-City-CSV_20190618/GeoLite2-City-Blocks-IPv4.csv', assume_missing=True, usecols=used_cols)
    df = df.dropna()
    df = df.astype(dtype=types)  # "reduce resolution"

    print(df.head(100), df.dtypes, df.index, sep='\n')
    uri = 'postgresql://geodatauser:password@localhost/geodata'
    with progress.ProgressBar():
        dd.to_sql(df, 'heatmapAPI_geonode', uri, if_exists='append', index=False, parallel=True)
    sys.exit(0)
