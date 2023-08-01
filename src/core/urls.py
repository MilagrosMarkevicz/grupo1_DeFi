<<<<<<< HEAD
from django.urls import path,include
=======
from django.urls import path, include
>>>>>>> ad4bde6a87cb55703e633a2843556956b3c8b2cf
from core import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
<<<<<<< HEAD
    path('index/', views.indexView, name='index'),
    path ('publicaciones/', views.publicacionesView, name='publicaciones'),
    path ('contacto/', views.contactoView, name= 'contacto'),
    path('usuarios/', include('usuarios.urls'))
=======
    path('', views.indexView, name = 'index'),
    path('publicaciones/', include('publicaciones.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('contacto/', views.contactoView, name = 'contacto'),
>>>>>>> ad4bde6a87cb55703e633a2843556956b3c8b2cf
]

urlpatterns += staticfiles_urlpatterns ()
