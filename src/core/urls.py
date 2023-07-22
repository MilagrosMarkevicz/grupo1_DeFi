from django.contrib import admin
from django.urls import path
from core import views



urlpatterns = [
    path('', views.indexView, name='index'),
    path('usuario/', views.usuarioView, name='usuario'),
    path('contacto/', views.contactosView, name='contacto'),
    path('registrarse/', views.registrarseView, name='registrarse'),
    path('iniciar sesion/', views.iniciarSesionView, name='iniciar sesion'),
    path('cerrar sesion/', views.cerrarSesionView, name='cerrar sesion'),
]
