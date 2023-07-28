from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from publicaciones.models import Publicaciones, Comentario
from .forms import CrearPublicacionForm, ComentarioForm
from core.mixins import SuperUsuarioAutorMixin, ColaboradorMixin
from django.db.models import Q

# View basada en una clase que renderiza las publicaciones
class VerPublicaciones(ListView):
    model = Publicaciones
    template_name = 'publicaciones.html'
    context_object_name = 'posteos'

    def get_queryset(self):
        consulta_anterior = super().get_queryset()

        categoria_id = self.request.GET.get('categoria')
        if categoria_id:
            consulta_anterior = consulta_anterior.filter(categoria__id=categoria_id)

        query = self.request.GET.get('q')
        if query:
            consulta_anterior = consulta_anterior.filter(
                Q(titulo__icontains=query) | Q(contenido__icontains=query)
            )

        ordenar_antiguedad = self.request.GET.get('ordenar_antiguedad')
        if ordenar_antiguedad == 'asc':
            consulta_anterior = consulta_anterior.order_by('fecha')
        elif ordenar_antiguedad == 'desc':
            consulta_anterior = consulta_anterior.order_by('-fecha')

        ordenar_alfabeticamente = self.request.GET.get('ordenar_alfabeticamente')
        if ordenar_alfabeticamente == 'asc':
            consulta_anterior = consulta_anterior.order_by('titulo')
        elif ordenar_alfabeticamente == 'desc':
            consulta_anterior = consulta_anterior.order_by('-titulo')

        return consulta_anterior
    
# View que crea posteos nuevos
class Postear(ColaboradorMixin, LoginRequiredMixin, CreateView):
    model = Publicaciones
    template_name = 'src/postear.html'
    form_class = CrearPublicacionForm

    def get_success_url(self):
        return reverse('publicaciones:publicaciones')

    def form_valid(self, form):
        form.instance.creador = self.request.user
        return super().form_valid(form)

# View que actualiza una publicacion ya existente
class EditarPost(SuperUsuarioAutorMixin, LoginRequiredMixin, UpdateView):
    model = Publicaciones
    template_name = 'src/editar-post.html'
    form_class = CrearPublicacionForm

    def get_success_url(self):
        return reverse('publicaciones:publicaciones')

# View que elimina un posteo
class EliminarPost(SuperUsuarioAutorMixin, LoginRequiredMixin, DeleteView):
    template_name = 'src/eliminar-post.html'
    model = Publicaciones

    def get_success_url(self):
        return reverse('publicaciones:publicaciones')

# View que permite ver los detalles de una publicacion
class PostDetalle(LoginRequiredMixin, DetailView):
    template_name = 'src/detalle-post.html'
    model = Publicaciones
    context_object_name = 'post'

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
            comentario = form.save(commit=False)
            comentario.autor = self.request.user
            comentario.post = publicacion
            comentario.save()
        return super().get(request)

class BorrarComentarioView(SuperUsuarioAutorMixin, LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = 'src/borrar-comentario.html'

    def get_success_url(self):
        return reverse('publicaciones:detalle-post', args=[self.object.post.id])
