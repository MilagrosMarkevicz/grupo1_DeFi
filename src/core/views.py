from django.shortcuts import render

# Create your views here.

def indexView(request):
    return render (request, 'index.html', {})

def publicacionesView (request):
    return render (request, 'publicaciones.html', {})

def contactoView (request):
    return render (request, 'contacto.html', {}) 