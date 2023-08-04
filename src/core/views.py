from django.shortcuts import render
from publicaciones.models import Publicaciones

# Create your views here

#View que renderiza la página de inicio
def indexView(request):
    # Recupera las últimas publicaciones ordenadas por fecha de publicación
    ultimas_publicaciones = Publicaciones.objects.order_by('-fecha')[:5]
    return render(request, 'index.html', {'ultimas_publicaciones': ultimas_publicaciones})



def acercadeView(request):
    return render(request, 'nosotros.html', {})


def defiView (request):
    return render (request, 'defi.html')

def blockView (request):
    return render (request, 'blockchains.html', {})

def tokensView (request):
    return render (request, 'tokens.html', {})

def tradingView (request):
    return render (request, 'trading.html', {})
