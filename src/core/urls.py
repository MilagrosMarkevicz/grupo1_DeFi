from django.urls import path, include
from core import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('index/', views.indexView, name='index'),
    path ('post/', views.postView, name='post'),
    path ('contacto/', views.contactoView, name= 'contacto'),
    path('usuarios/', include('usuarios.urls'))
]

urlpatterns += staticfiles_urlpatterns ()
