from .base import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'juanjl28$default',
        'USER': 'juanjl28',
        'PASSWORD': 'agosto1126',
        'HOST': 'juanjl28.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}