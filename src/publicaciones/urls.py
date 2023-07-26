from django.urls import path
from .views import PublicacionListView, PublicacionCreateUpdateView, PublicacionDeleteView, FiltrarPublicacionesView

app_name = 'publicaciones'

urlpatterns = [
    path('publicaciones/', PublicacionListView.as_view(), name='publicaciones'),
    path('publicaciones/crear/', PublicacionCreateUpdateView.as_view(), name='crear-publicacion'),
    path('publicaciones/editar/<int:pk>/', PublicacionCreateUpdateView.as_view(), name='editar-publicacion'),
    path('publicaciones/eliminar/<int:pk>/', PublicacionDeleteView.as_view(), name='eliminar-publicacion'),
    path('publicaciones/filtrar/', FiltrarPublicacionesView.as_view(), name='filtrar-publicaciones'),
]
