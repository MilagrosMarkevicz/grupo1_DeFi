from django.shortcuts import render

# Create your views here.

def usuarioView(request):
    return render(request, 'usuario.html', {})

def registrarseView(request):
    return render(request, 'registrarse.html', {})

def iniciarSesionView(request):
    return render(request, 'iniciar-sesion.html', {})

def cerrarSesionView(request):
    return render(request, 'cerrar-sesion.html', {})