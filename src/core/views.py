from django.shortcuts import render

# Create your views here.

def indexView(request):
    return render(request, 'index.html', {})

def usuarioView(request):
    return render(request, 'usuario.html', {})

def contactoView(request):
    return render(request, 'contacto.html', {})

def registrarseView(request):
    return render(request, 'registrarse.html', {})

def iniciarSesionView(request):
    return render(request, 'iniciar-sesion.html', {})

def cerrarSesionView(request):
    return render(request, 'cerrar-sesion.html', {})

