from django.urls import path
from .views import index, nosotros, catalogo, catalogo2, formulario, producto1, producto2, producto3, producto4, producto5, producto6, producto7, producto8

urlpatterns = [
    path('',index,name='index'),
    path('index.html',index,name='index'),
    path('Nosotros.html',nosotros,name='nosotros'),
    path('Catalogo.html',catalogo,name='catalogo'),
    path('Catalogo2.html',catalogo2,name='catalogo2'),
    path('Formulario.html',formulario,name='formulario'),
    path('Producto1.html',producto1,name='producto1'),
    path('Producto2.html',producto2,name='producto2'),
    path('Producto3.html',producto3,name='producto3'),
    path('Producto4.html',producto4,name='producto4'),
    path('Producto5.html',producto5,name='producto5'),
    path('Producto6.html',producto6,name='producto6'),
    path('Producto7.html',producto7,name='producto7'),
    path('Producto8.html',producto8,name='producto8'),
]
