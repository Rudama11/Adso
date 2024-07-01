from django.urls import path
from app.views import*
from app.views.Categoria.views import *
from app.views.Ubicacion.views import *
from app.views.Proveedor.views import * 
# Define el namespace para la aplicación

app_name = 'app'

urlpatterns = [
    path('categoria/listar/', CategoriaListView.as_view(), name='categoria_listar'), 
    path('categoria/listar2/', lista_categoria, name='categoria_lista2' ),
    path('Ubicacion/listarU/', lista_ubicacion, name='ubicacion_listarU' ),
    path('Proveedor/listarP/', lista_Proveedor,name='Proveedores_listarP')
    
    # path('uno/', Vista1, name='Vista1'),
    # path('dos/', Vista2, name='Vista2'),  # Corregido el nombre a 'Vi44sta2'
]
