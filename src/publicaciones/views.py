from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Publicaciones, Comentario, Categoria
from .forms import PostForm, ComentarioForm
from core.mixins import SuperUsuarioAutorMixin, ColaboradorMixin
from django.db.models import Q

# View basada en una clase que renderiza las publicaciones
class VerPublicaciones(ListView):
    model = Publicaciones
    template_name = 'publicaciones.html'
    context_object_name = 'posteos'
    cats = Categoria.objects.all()
                
    def get_context_data(self, *args, **kwargs):
        menu_categoria = Categoria.objects.all()
        contexto = super(VerPublicaciones, self).get_context_data(*args, **kwargs)
        contexto["menu_categoria"] = menu_categoria
        return contexto
        
def categoriaListView(request):
    menu_categoria_list = Categoria.objects.all()
    return render(request, 'categoria_list.html', {'menu_categoria_list':menu_categoria_list})

def categoriaView(request, cats):
    category_posts = Publicaciones.objects.filter(categoria=cats.replace('-', ' '))
    return render(request, 'categoria.html', {'cats':cats.replace('-', ' ').title(), 'category_posts':category_posts})


# View que permite ver los detalles de una publicacion
class PostDetalle(LoginRequiredMixin, DetailView):
    template_name = 'detalle-post.html'
    model = Publicaciones
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        menu_categoria = Categoria.objects.all()
        contexto = super().get_context_data(**kwargs)
        contexto['formulario_comentario'] = ComentarioForm()
        contexto["menu_categoria"] = menu_categoria
        return contexto

    def post(self, request, pk):
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

class AgregarCategoriaView(LoginRequiredMixin, CreateView):
	model = Categoria
	template_name = 'agregar_categoria.html'
	fields = '__all__' 
        
        
# View que crea posteos nuevos
class Postear(LoginRequiredMixin, ColaboradorMixin, CreateView):
    model = Publicaciones
    template_name = 'postear.html'
    form_class = PostForm
    
    def get_success_url(self):
        return reverse('publicaciones:postear.html')
    
    def form_valid(self, form):
        f = form.save(commit=False)
        f.creador_id = self.request.user.id
        return super().form_valid(f)
       
   
class PostearView(LoginRequiredMixin, ColaboradorMixin, CreateView):
        
    def get(self, request):
        form = PostForm()
        return render(request, 'postear.html', {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.creador_id = request.user.id
            post.save()
            return redirect('publicaciones:publicaciones')
        return render(request, 'postear.html', {'form': form})


#	model = Publicaciones
#	form_class = PostForm
#	template_name = 'postear.html'
#	#fields = ('title', 'body')

# View que actualiza una publicacion ya existente
class EditarPost(LoginRequiredMixin, SuperUsuarioAutorMixin, ColaboradorMixin, UpdateView):
    model = Publicaciones
    template_name = 'editar-post.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('publicaciones:publicaciones')

# View que elimina un posteo
class EliminarPost(LoginRequiredMixin, SuperUsuarioAutorMixin, DeleteView):
    template_name = 'eliminar-post.html'
    model = Publicaciones

    def get_success_url(self):
        return reverse('publicaciones:publicaciones')



class BorrarComentarioView(LoginRequiredMixin, SuperUsuarioAutorMixin, DeleteView):
    model = Comentario
    template_name = 'borrar-comentario.html'

    def get_success_url(self):
        return reverse('publicaciones:detalle-post', args=[self.object.post.id])
    

class EditarComentarioView(LoginRequiredMixin, SuperUsuarioAutorMixin, UpdateView):
    model = Comentario

    template_name = 'editar-comentario.html'

    form_class = ComentarioForm

    def get_success_url(self):
        return reverse('publicaciones:detalle-post', args=[self.object.post.id])

    
