from .base import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MilagrosMarkevic$default',
        'USER': 'MilagrosMarkevic',
        'PASSWORD': 'milagros150597',
        'HOST': 'MilagrosMarkevicz.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}