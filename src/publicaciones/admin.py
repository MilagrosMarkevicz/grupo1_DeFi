
from django.contrib import admin
from publicaciones.models import Publicaciones
from publicaciones.models import Categoria
from publicaciones.models import Comentario

# Register your models here.

admin.site.register(Publicaciones)
admin.site.register(Categoria)
admin.site.register(Comentario)

