from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    telefono = models.CharField(max_length=20)
    es_admin = models.BooleanField(default=False) 
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuarios_custom',
        blank=True,
        help_text='Los grupos a los que pertenece este usuario. Un usuario obtiene todos los permisos de sus grupos.',
        verbose_name='grupos',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuarios_custom',
        blank=True,
        help_text='Permisos específicos para este usuario.',
        verbose_name='permisos de usuario',
    )      