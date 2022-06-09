from django.shortcuts import render

# Create your views here.

#definir nuestro home, que sera index


def index(request):
    
    return render(request, 'core/index.html')


def nosotros(request):
    
    return render(request, 'core/Nosotros.html')


def catalogo(request):
    
    return render(request, 'core/Catalogo.html')


def formulario(request):
    
    return render(request, 'core/Formulario.html')

