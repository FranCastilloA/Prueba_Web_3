from django.shortcuts import render

# Create your views here.

#definir nuestro home, que sera index


def index(request):
    
    return render(request, 'core/index.html')


def nosotros(request):
    
    return render(request, 'core/Nosotros.html')


def catalogo(request):
    
    return render(request, 'core/Catalogo.html')

def catalogo2(request):
    
    return render(request, 'core/Catalogo2.html')

def formulario(request):
    
    return render(request, 'core/Formulario.html')

def producto1(request):
    
    return render(request, 'core/Producto1.html')

def producto2(request):
    
    return render(request, 'core/Producto2.html')

def producto3(request):
    
    return render(request, 'core/Producto3.html')

def producto4(request):
    
    return render(request, 'core/Producto4.html')

def producto5(request):
    
    return render(request, 'core/Producto5.html')

def producto6(request):
    
    return render(request, 'core/Producto6.html')

def producto7(request):
    
    return render(request, 'core/Producto7.html')

def producto8(request):
    
    return render(request, 'core/Producto8.html')