from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contacto(models.Model):
    autor = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'mensaje_usuario')
    asunto = models.CharField(max_length=150)
    mensaje = models.TextField()
    fecha = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.asunto + '-' + self.autor.username
