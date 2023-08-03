from django.shortcuts import render
from publicaciones.models import Publicaciones

# Create your views here

#View que renderiza la página de inicio
def indexView(request):
    return render(request, 'index.html', {'posteos':Publicaciones.objects.all().order_by('fecha')})





