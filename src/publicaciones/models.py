from django.db import models
from usuarios.models import User
# from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

#Esta clase crea una tabla para las categorías

class Categoria(models.Model):
    nombre = models.CharField(max_length= 255)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('publicaciones:publicaciones')

#Esta clase crea una tabla para las publicaciones
class Publicaciones(models.Model):
    fecha = models.DateTimeField(auto_now_add = True)
    update = models.DateField(auto_now = True)
    titulo = models.CharField(max_length= 255)
    post = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL, null = True, blank = True, related_name = 'posteos_categoria')
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True, related_name='posteos_creador')
    imagen_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.titulo + '-' + self.creador.username
    
    def get_absolute_url(self):
        return reverse('publicaciones')
        
    

class Comentario(models.Model):
    texto = models.TextField()
    fecha = models.DateField(auto_now_add= True)
    post = models.ForeignKey(Publicaciones, on_delete= models.CASCADE, related_name= 'comentarios')
    autor = models.ForeignKey(User, on_delete= models.CASCADE, related_name= 'comentarios_autor')


    def __str__(self):
        return self.post.titulo + '-' + self.autor.first_name
    
 


    
        