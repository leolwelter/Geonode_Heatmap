# API for geonodes-map.info

## Installing
1. clone the repo
2. create IPHeatmap/settings_local.py using the template provided
3. create a virtual environment for python > 3.5
    * instructions can be found [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
4. activate the environment and install required packages with ```pip install -r requirements.txt```
5. Get your database in the right shape with ```python manage.py migrate```
6. Add necessary data from "GeoLite2 City CSV 2019" (not included here)
   * specifically, City Blocks IPv4
7. Run ```clean_data_and_load.sh``` to do exactly what it says

## Running
1. Activate your venv: ```source venv/bin/activate```
2. Run the script ```daemonize_gunicorn.sh``` 
   * If something goes wrong, be sure to kill all runaway processes (pgrep/pkill are your friends)
3. Make changes as you like
4. Restart the gunicorn process with ```restart-supervisor.sh```

## Credits/Acknowledgements
I couldn't have made this without the wonderful folks at Django, and the great Django Rest Framework/Filters packages.
Additionally, Dask is great and I'd highly recommend it for your data cleaning.