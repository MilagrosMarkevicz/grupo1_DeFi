from django.shortcuts import render

# View que renderiza la página de inicio
def indexView(request):
    return render(request, 'index.html', {})

# View que renderiza la página de contacto
def contactoView(request):
    return render(request, 'contacto.html', {})

# View que renderiza la página de publicaciones
def publicacionesView(request):
    return render(request, 'publicaciones.html', {})


