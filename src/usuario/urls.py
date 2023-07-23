from django.urls import path
from usuario import views

app_name = "usuario"

urlpatterns = [
    path('usuario', views.usuarioView, name = 'usuario'), 
    path('registrarse/', views.registrarseView, name='registrarse'),
    path('iniciar sesion/', views.iniciarSesionView, name='iniciar sesion'), 
     path('cerrar sesion/', views.cerrarSesionView, name='cerrar sesion'),
]
