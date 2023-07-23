from django.contrib import admin
from django.urls import path
from core import views



urlpatterns = [
    path('', views.indexView, name='index'),
    path('contacto/', views.contactoView, name='contacto'),
]
