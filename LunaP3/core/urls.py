from django.urls import path
from .views import index, nosotros, catalogo, formulario

urlpatterns = [
    path('',index,name='index'),
    path('index.html',index,name='index'),
    path('Nosotros.html',nosotros,name='nosotros'),
    path('Catalogo.html',catalogo,name='catalogo'),
    path('Formulario.html',formulario,name='formulario'),
]
