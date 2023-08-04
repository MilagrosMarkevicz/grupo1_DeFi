from django.shortcuts import render

# Create your views here

#View que renderiza la página de inicio
def indexView(request):
    return render(request, 'index.html', {})

def contactoView(request):
    return render(request, 'contacto.html', {})

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
