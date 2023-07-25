from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User (AbstractUser):
    telefono = models.CharField(max_length=20)
    es_admin = models.BooleanField(default=False) 
         