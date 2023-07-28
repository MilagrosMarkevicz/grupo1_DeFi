from django.shortcuts import render

# Create your views here

#View que renderiza la página de inicio
def indexView(request):
    return render(request, 'index.html', {})




