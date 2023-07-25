from django.urls import path,include
from core import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('index/', views.indexView, name='index'),
    path ('publicaciones/', views.publicacionesView, name='publicaciones'),
    path ('contacto/', views.contactoView, name= 'contacto'),
    path('', include('usuario.urls'))
]

urlpatterns += staticfiles_urlpatterns ()