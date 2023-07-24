from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Usuario(AbstractUser):
    telefono=models.CharField(max_length=255)
    domicilio=models.CharField(max_length=255,blank=True,null=True)
    es_colaborador=models.BooleanField(default=False)