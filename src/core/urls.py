from django.urls import path
from core import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('index/', views.indexView, name='index'),
    path ('post/', views.postView, name='post'),
    path ('contacto/', views.contactoView, name= 'contacto'),
    path ('publicaciones/', views.publicacionesView, name='publicaciones'),
    path ('defi/', views.defiView, name= 'defi'),
    path ('blockchains/', views.blockView, name='blockchains'),
    path ('nosotros/', views.nosotrosView, name= 'nosotros'),
    path ('tokens/', views.tokensView, name='tokens'),
    path ('trading/', views.tradingView, name='trading'),
]

urlpatterns += staticfiles_urlpatterns ()