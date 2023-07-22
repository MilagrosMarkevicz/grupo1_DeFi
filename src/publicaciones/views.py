from django.shortcuts import render


# Create your views here.


def publicacionesView(request):
    return render(request, 'publicaciones.html', {})
