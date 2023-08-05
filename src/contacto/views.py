from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Contacto
from .forms import ContactoForm


class Contactar(LoginRequiredMixin, CreateView):
    model = Contacto

    template_name = 'contactar.html'

    form_class = ContactoForm

    def get_success_url(self):
        return reverse('index')
    
    def form_valid(self, form):
        f = form.save(commit=False)
        f.autor_id = self.request.user.id
        return super().form_valid(f)
