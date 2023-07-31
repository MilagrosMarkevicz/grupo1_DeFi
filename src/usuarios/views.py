from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from .forms import RegistrarseFrom
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Profile

class LoginUsuario(LoginView):
    template_name = 'usuarios/login.html'


class RegistroView(CreateView):
    template_name = 'usuarios/registrarse.html'
    form_class = RegistrarseFrom
    success_url = reverse_lazy('index')

class ShowProfilePageView(DetailView):
	model = Profile
	template_name = 'registration/user_profile.html'

	def get_context_data(self, *args, **kwargs):
		#users = Profile.objects.all()
		context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
		
		page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

		context["page_user"] = page_user
		return context

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
    
