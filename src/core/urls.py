from django.urls import path, include
from core import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('index/', views.indexView, name='index'),
    path('publicaciones/', views.publicacionesView, name='publicaciones'),
    path('contacto/', views.contactoView, name='contacto'),
    path('usuarios/', include('usuarios.urls')),
    # No se necesita duplicar las rutas anteriores, por lo que elimino estas líneas:
    # path('', views.indexView, name='index'),
    # path('publicaciones/', include('publicaciones.urls')),
    # path('usuarios/', include('usuarios.urls')),
    # path('contacto/', views.contactoView, name='contacto'),
]

urlpatterns += staticfiles_urlpatterns()
