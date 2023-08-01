from django.urls import path
<<<<<<< HEAD

from django.contrib.auth.views import LoginView, LogoutView

=======
from django.contrib.auth.views import LoginView, LogoutView
>>>>>>> ad4bde6a87cb55703e633a2843556956b3c8b2cf
from .views import RegistroView, EliminarUsuario,EditarUsuario


app_name= 'usuarios'

urlpatterns=[
    path('login/',LoginView.as_view(template_name = 'usuarios/login.html'),name = 'login'),
<<<<<<< HEAD
    path('logout/', LogoutView.as_view(next_page='../login'),name = 'logout'),
    path('registrarse/', RegistroView.as_view(),name = 'registrarse'),
=======
    path('logout/', LogoutView.as_view(next_page=''),name = 'logout'),
    path('registrarse/', RegistroView.as_view(), name = 'registrarse'),
>>>>>>> ad4bde6a87cb55703e633a2843556956b3c8b2cf
    path('editar_usuario/<int:pk>', EditarUsuario.as_view(),name = 'editar_usuario'),
    path('eliminar_usuario/<int:pk>', EliminarUsuario.as_view(), name= 'eliminar_usuario')
]


