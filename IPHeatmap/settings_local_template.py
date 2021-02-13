from typing import List

SECRET_KEY = str

DEBUG = bool

ALLOWED_HOSTS = List[str]

DATABASES = {
    'default': {
        'ENGINE': str,
        'NAME': str,
        'USER': str,
        'PASSWORD': str,
        'HOST': str,
        'CONN_MAX_AGE': int,  # seconds
        'PORT': str
    }
}
