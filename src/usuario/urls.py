from django.urls import path
from usuario import views

app_name = "usuario"

urlpatterns = [
    path('usuario', views.usuarioView, name = 'usuario'),  
]
