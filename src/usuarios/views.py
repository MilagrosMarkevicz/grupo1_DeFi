from django.shortcuts import render

from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .forms import RegistrarseFrom

from django.contrib.auth.forms import UserCreationForm

from .models import User

from django.contrib.auth.mixins import LoginRequiredMixin 

from django.contrib.auth import login

from django.urls import reverse

from django.contrib.auth.views import LoginView


# Create your views here.

class LoginUsuario(LoginView):
    template_name = 'usuarios/login.html'


class RegistroView(CreateView):
    model = User
    template_name = 'usuarios/registros.html'
    form_class = RegistrarseFrom
    def get_success_url(self):
        return reverse ('index')


    def form_valid(self,form):

        respuesta = super().form_valid(form)

        usuario = form.save()

        login(self.request, usuario)

        return respuesta




class EliminarUsuario(DeleteView, LoginRequiredMixin):
    template_name = 'usuarios/eliminar_usuario.html'

    model = User

    def get_success_url(self):
        return reverse('usuarios:login')