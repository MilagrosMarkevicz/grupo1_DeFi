from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView

from .forms import RegistrarseFrom


from .models import User

from django.contrib.auth.mixins import LoginRequiredMixin 

from django.contrib.auth import login

from django.urls import reverse

from .forms import EditarUserForm


# Create your views here.



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



class EditarUsuario(UpdateView, LoginRequiredMixin):
    model = User

    template_name = 'usuarios/editar_usuario.html'

    form_class = EditarUserForm


    def form_valid(self, form):

        respuesta = super().form_valid(form)
        usuario = form.save()

        login(self.request,usuario)

        return respuesta


    def get_success_url(self):
        return reverse('index')



    model = User

    def get_success_url(self):
        return reverse('usuarios:login')
    
