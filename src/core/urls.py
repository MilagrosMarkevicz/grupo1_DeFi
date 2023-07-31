from django.urls import path, include
from core import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.indexView, name = 'index'),
    path('publicaciones/', include('publicaciones.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('contacto/', views.contactoView, name = 'contacto'),
]

urlpatterns += staticfiles_urlpatterns ()
