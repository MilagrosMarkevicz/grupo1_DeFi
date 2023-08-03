from django.shortcuts import render
from publicaciones.models import Publicaciones

# Create your views here

#View que renderiza la página de inicio
def indexView(request):
    # Recupera las últimas publicaciones ordenadas por fecha de publicación
    ultimas_publicaciones = Publicaciones.objects.order_by('-fecha')[:5]
    return render(request, 'index.html', {'ultimas_publicaciones': ultimas_publicaciones})





