from typing import Optional
from django.contrib.auth.mixins import UserPassesTestMixin

class SuperUsuarioAutorMixin(UserPassesTestMixin):
    def test_func(self):
        usuario = self.request.user
        obj = self.get_object()


#Acá entra si se trata de una publicación, por la columna creador
        if hasattr(obj, 'creador'):
            return usuario == obj.creador or usuario.is_superuser
        
#Acá entra si se trata de un comentario, por la columna autor
        if hasattr(obj, 'autor'):
            return usuario == obj.autor or usuario.is_superuser or usuario == obj.post.creador
        

class ColaboradorMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser