import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1  # recommended setting from gunicorn docs
# bind = ['127.0.0.1:8000']
bind = ['0.0.0.0:8000']
worker_class = 'gevent'  # sync, gthread, gevent, eventlet, tornado, etc.
