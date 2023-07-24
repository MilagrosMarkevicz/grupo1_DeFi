from django.shortcuts import render

from django.views.generic.edit import CreateView, DeleteView, UpdateView

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from django.contrib.auth.mixins import LoginRequiredMixin 

from django.contrib.auth import login

from django.urls import reverse

# Create your views here.

class RegistroView(CreateView):
    model = User

    template_name = 'usuarios/registro.html'

    form_class = UserCreationForm


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