from django.urls import path
from publicaciones import views

app_name= "publicaciones"

urlpatterns = [
    path("publicaciones/",views.VerPublicaciones.as_views(),name="publicaciones"),
    path("editar-Post/<int:pk>",views.EditarPost.as_views(),name="editar-post"),
    path("publicaciones-ordenadas/",views.VerPublicacionesOrdenAlfabetico.as_views(),name="publicaciones-ordenadas"),
    path("publicaciones-categoria/",views.VerPublicacionesPorCategoria.as_views(),name="publicaciones-por-categoria"),
    path("postear/",views.Postear.as_views(),name="postear"),
    path("editar-Post/<int:pk>",views.EditarPost.as_views(),name="editar-post"),
    path("eliminar-post/<int:pk>",views.EminarPost.as_views(),name="eliminar-post"),
    path("detalle-post/<int:pk>",views.DetallePost.as_views(),name="detalle-post"),
    path("borrar-comentario/<int:pk>",views.BorrarComentario.as_views(),name="borrar-comentario")
    
]
