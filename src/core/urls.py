from django.urls import path, include
from core import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.indexView, name = 'index'),
    path('publicaciones/', include('publicaciones.urls')),
    path('usuarios/', include('usuarios.urls')),
<<<<<<< HEAD
    path('contacto/', views.contactoView, name = 'contacto'),
    path('acercade/', views.acercadeView, name = 'acercade'),
    path ('defi/', views.defiView, name= 'defi'),
    path ('blockchains/', views.blockView, name='blockchains'),
    path ('tokens/', views.tokensView, name='tokens'),
    path ('trading/', views.tradingView, name='trading'),
=======
    path('contacto/', include('contacto.urls')),
>>>>>>> editar_usuarios
]

urlpatterns += staticfiles_urlpatterns ()
