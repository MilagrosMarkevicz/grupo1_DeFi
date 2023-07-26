from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.db.models import Q
from .models import Publicaciones, Categoria, Comentario
from .forms import CrearPublicacionForm, ComentarioForm
from core.mixins import SuperUsuarioAutorMixin, ColaboradorMixin

class PublicacionListView(LoginRequiredMixin, ListView):
    model = Publicaciones
    template_name = 'src/publicaciones.html'
    context_object_name = 'posteos'
    form_class = CrearPublicacionForm

    def get_queryset(self):
        categoria_id = self.request.GET.get('categoria')
        query = self.request.GET.get('q')

        consulta_anterior = super().get_queryset()

        if categoria_id:
            categoria = get_object_or_404(Categoria, id=categoria_id)
            consulta_anterior = consulta_anterior.filter(categoria=categoria)

        if query:
            consulta_anterior = consulta_anterior.filter(
                Q(titulo__icontains=query) | Q(contenido__icontains=query)
            )

        consulta_ordenada = consulta_anterior.order_by('fecha')
        return consulta_ordenada

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        context['form'] = self.form_class()
        return context

class PublicacionCreateUpdateView(SuperUsuarioAutorMixin, ColaboradorMixin, LoginRequiredMixin, View):
    form_class = CrearPublicacionForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.creador = request.user
            f.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'errors': form.errors})

class PublicacionDeleteView(SuperUsuarioAutorMixin, ColaboradorMixin, LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        publicacion = get_object_or_404(Publicaciones, id=kwargs['pk'])
        publicacion.delete()
        return JsonResponse({'success': True})

class FiltrarPublicacionesView(LoginRequiredMixin, ListView):
    model = Publicaciones
    template_name = 'publicaciones.html'
    context_object_name = 'posteos'
    form_class = CrearPublicacionForm