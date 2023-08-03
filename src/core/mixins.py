#from typing import Optional
#from django.contrib.auth.mixins import UserPassesTestMixin


#class SuperusuarioAutorMixin(UserPassesTestMixin):
 #   def test_func(self) :
  #      usuario=self.request.user
   #     obj=self.get_object()
        #recupera el objeto completo y lo guarda


    #    if hasattr(obj,'creador'): #aca entra si es una publicacion

     #     return user== obj.creador or usuario.is_superuser #consulta si el que publico es el que quiere borrar o si es 1 super usuario
      #  if hasattr(obj,"autor"):# aca entra si es 1 comentario
       #    return usuario== obj.autor or usuario.is_superuser or usuario==obj.post.creador #accsede a 1 comentario de 1 publicacion
                                                                                           #la dueña de la publicacion tambien puede borrar
                                                                                           #el comentario de ot
                                                                                           # ra persona.
#class ColaboradorMixin(UserPassesTestMixin):
 #  def test_func(self):
  #    return self.request.user.is_staff or self.request.user.is_superuser

from typing import Optional
from django.contrib.auth.mixins import UserPassesTestMixin

class SuperUsuarioAutorMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        obj = self.get_object()


#Acá entra si se trata de una publicación, por la columna creador
        if hasattr(obj, 'creador'):
            return user == obj.creador or user.is_superuser
        
#Acá entra si se trata de un comentario, por la columna autor
        if hasattr(obj, 'autor'):
            return user == obj.autor or user.is_superuser or user== obj.post.creador
        

class ColaboradorMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser