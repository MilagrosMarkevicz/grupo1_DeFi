from django.urls import path
from publicaciones import views

app_name= 'publicaciones'

urlpatterns = [
    path('publicaciones/',views.VerPublicaciones.as_view(),name='publicaciones'),

    path('postear/',views.Postear.as_view(),name='postear'),
    
    path('editar-post/<int:pk>',views.EditarPost.as_view(),name='editar-post'),

    path('eliminar-post/<int:pk>',views.EliminarPost.as_view(),name='eliminar-post'),

    path('detalle-post/<int:pk>',views.PostDetalle.as_view(),name='detalle-post'),

    path('borrar-comentario/<int:pk>', views.BorrarComentarioView.as_view(), name = 'borrar-comentario'),

    path('publicaciones-ordenadas/',views.VerPublicacionesOrdenAlfabetico.as_view(),name='publicaciones-ordenadas'),

    path('publicaciones-ordenadas-desc/',views.VerPublicacionesOrdenAlfabeticoDesc.as_view(),name='publicaciones-ordenadas-desc'),

    path('publicaciones-categoria/',views.VerPublicacionesPorCategoria.as_view(),name='publicaciones-por-categoria'),

   
    
  
  

    
]
