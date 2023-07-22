from django.shortcuts import render

# Create your views here.

def usuarioView(request):
    return render(request, 'usuario.html', {})