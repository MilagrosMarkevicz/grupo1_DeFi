from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from publicaciones.models import Publicaciones, Categoria
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import CrearPublicacionForm, ComentarioForm, Comentario
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from core.mixins import SuperUsuarioAutorMixin, ColaboradorMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404 
# Create your views here.

# View basada en una clase que renderiza las publicaciones

class VerPublicaciones(LoginRequiredMixin ,ListView):
    model = Publicaciones
    template_name = 'publicaciones/publicaciones.html'
    context_object_name = 'posteos'


    def get_queryset(self):
        consulta_anterior = super().get_queryset()

        consulta_ordenada = consulta_anterior.order_by('fecha')
        return consulta_ordenada

class VerPublicacionesPorCategoria(LoginRequiredMixin, ListView):
    template_name = 'publicaciones/publicaciones.html'
    context_object_name = 'posteos'

    def publicaciones_por_categoria(request, categoria_id):
        categoria = get_object_or_404(Categoria, id=categoria_id)
        publicaciones = Publicaciones.objects.filter(categoria=categoria)
        return render(request, 'publicaciones_por_categoria.html', {'categoria': categoria, 'publicaciones': publicaciones})

    def get_queryset(self):
        categoria = get_object_or_404(Categoria, nombre=self.kwargs['nombre_categoria'])
        consulta_anterior = Publicaciones.objects.filter(categoria=categoria)
        consulta_ordenada = consulta_anterior.order_by('-fecha')  # Ordenar por antigüedad descendente
        return consulta_ordenada

class VerPublicacionesOrdenAlfabetico(LoginRequiredMixin, ListView):
    template_name = 'publicaciones/publicaciones.html'
    context_object_name = 'posteos'

    def get_queryset(self):
        consulta_anterior = Publicaciones.objects.all()
        consulta_ordenada = consulta_anterior.order_by('titulo')  # Ordenar por título ascendente
        return consulta_ordenada

class VerPublicacionesOrdenAlfabeticoDesc(LoginRequiredMixin, ListView):
    template_name = 'publicaciones/publicaciones.html'
    context_object_name = 'posteos'

    def get_queryset(self):
        consulta_anterior = Publicaciones.objects.all()
        consulta_ordenada = consulta_anterior.order_by('-titulo')  # Ordenar por título descendente
        return consulta_ordenada


# View que crea posteos nuevos

class Postear(ColaboradorMixin, LoginRequiredMixin, CreateView):
    model = Publicaciones
    template_name = 'publicaciones/postear.html'
    form_class = CrearPublicacionForm

    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
    
    def form_valid(self, form):
        f = form.save(commit= False) #Le paré el carro al form para que no guarde todavía.
        f.creador_id = self.request.user.id
        return super().form_valid(f)
    
# View que actualiza una publicacion ya existente

class EditarPost(SuperUsuarioAutorMixin, LoginRequiredMixin, UpdateView):
    model = Publicaciones
    template_name = 'Publicaciones/editar-post.html'
    form_class = CrearPublicacionForm

    def get_success_url(self):
        return reverse('publicaciones:publicaciones')
    
# View que elimina un posteo

class EliminarPost(SuperUsuarioAutorMixin, LoginRequiredMixin, DeleteView):
    template_name = 'publicaciones/eliminar-post.html'
    model = Publicaciones
    
    def get_success_url(self):
        return reverse('publicaciones:publicaciones')

# View que permite ver los detalles de una publicacion

class PostDetalle(LoginRequiredMixin, DetailView):
    template_name = 'publicaciones/detalle-post.html'
    model = Publicaciones
    context_object_name = 'post'

# Método get 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['formulario_comentario'] = ComentarioForm()
        return context

    def post(self, request, *args, **kwargs):

        if not self.request.user.is_authenticated:
            return reverse('usuarios:login')
    
        
        publicacion = self.get_object()
        form = ComentarioForm(request.POST)

        if form.is_valid():
            comentario = form.save(commit= False)
            comentario.autor_id = self.request.user.id
            comentario.post = publicacion
            comentario.save()
            return super().get(request)
        else:
            return super().get(request)
        

class BorrarComentarioView(SuperUsuarioAutorMixin, LoginRequiredMixin, DeleteView):
        model = Comentario
        template_name = 'publicaciones/borrar-comentario.html'

        def get_success_url(self):
            return reverse('publicaciones:detalle-post', args =[self.object.post.id])
