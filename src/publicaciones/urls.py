from django.contrib import admin
from django.urls import path
from publicaciones import views
from .views import PostearView

app_name = 'publicaciones'

urlpatterns = [
    path('publicaciones/', views.VerPublicaciones.as_view(), name = 'publicaciones'),
   # path('postear/', PostearView.as_view(), name='add_post'),
    path('postear/', PostearView.as_view(), name='postear'),
    path('editar-post/<int:pk>', views.EditarPost.as_view(), name = 'editar-post'),
    path('eliminar-post/<int:pk>', views.EliminarPost.as_view(), name = 'eliminar-post'),
    path('detalle-post/<int:pk>', views.PostDetalle.as_view(), name = 'detalle-post'),
    path('borrar-comentario/<int:pk>', views.BorrarComentarioView.as_view(), name = 'borrar-comentario'),
    path('editar-comentario/<int:pk>', views.EditarComentarioView.as_view(),name = 'editar-comentario' ),
    path('agregar_categoria/', views.AgregarCategoriaView.as_view(), name= 'agregar_categoria'),
    
]


