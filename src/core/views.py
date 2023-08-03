from django.shortcuts import render

# Create your views here

#View que renderiza la página de inicio
def indexView(request):
    return render(request, 'index.html', {})

def contactoView(request):
    return render(request, 'contacto.html', {})



def postView (request):
    return render (request, 'post.html', {})

def contactoView (request):
    return render (request, 'contacto.html', {}) 

def publicacionesView (request):
    return render (request, 'publicaciones.html', {})

def defiView (request):
    return render (request, 'defi.html')

def blockView (request):
    return render (request, 'blockchains.html', {})

def nosotrosView (request):
    return render (request, 'nosotros.html', {})

def tokensView (request):
    return render (request, 'tockens.html', {})

def tradingView (request):
    return render (request, 'trading.html', {})