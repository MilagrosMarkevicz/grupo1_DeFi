from django.shortcuts import render

# Create your views here.
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.views import LoginView
from .forms import RegistrarseFrom
# Create your views ere.

class LoginUsuario(LoginView):
    template_name = 'usuarios/login.html'


class RegistroView(CreateView):
    model = User
    template_name = 'usuarios/registros.html'
    form_class = RegistrarseFrom
    def get_success_url(self):
        return reverse ('index')


class EditarUsuario(UpdateView, LoginRequiredMixin):
    model = User

    template_name = 'usuarios/editar_usuario.html'

    form_class = UserCreationForm
    


    def form_valid(self, form):

        respuesta = super().form_valid(form)
        usuario = form.save()

        login(self.request,usuario)

        return respuesta


    def get_success_url(self):
        return reverse('index')
    


class EliminarUsuario(DeleteView, LoginRequiredMixin):
    template_name = 'usuarios/eliminar_usuario.html'

    model = User

    def get_success_url(self):
        return reverse('usuarios:login')