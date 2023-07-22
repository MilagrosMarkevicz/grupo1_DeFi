from django.urls import path
from core import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('index/', views.indexView, name='index'),
]

urlpatterns += staticfiles_urlpatterns ()