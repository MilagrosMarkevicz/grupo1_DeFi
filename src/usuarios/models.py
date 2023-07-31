from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, Group, Permission


class Profile(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.usuario)
    
    def get_absolute_url(self):
        return reverse('index')
    

class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='usuarios_users'  # Agrega related_name personalizado para evitar el conflicto
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='usuarios_users'  # Agrega related_name personalizado para evitar el conflicto
    )

    def __str__(self):
        return self.username