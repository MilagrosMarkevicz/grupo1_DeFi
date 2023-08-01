from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Profile(models.Model):
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.usuario)
    
    def get_absolute_url(self):
        return reverse('index')
    

