from django.shortcuts import render

from django.views.generic.edit import CreateView

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

# Create your views here.

class RegistroView(CreateView):
    model = User

    template_name = 'usuarios/registro.html'

    form_class = UserCreationForm


