from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User (AbstractUser):
    telefono = models.CharField(max_length=20)
    es_admin = models.BooleanField(default=False) 
         
=======
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
>>>>>>> ad4bde6a87cb55703e633a2843556956b3c8b2cf
