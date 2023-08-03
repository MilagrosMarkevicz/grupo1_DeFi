from django.urls import path
from .views import Contactar

app_name = "contacto"

urlpatterns = [
    path('contactar/',Contactar.as_view(), name = 'contactar')
]