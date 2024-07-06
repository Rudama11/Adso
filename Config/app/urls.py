from django.urls import path
from app.views import*
from app.views.Categoria.views import *
from app.views.Ubicacion.views import *
from app.views.Proveedor.views import * 
from app.views.Cliente.views import *

# Define el namespace para la aplicación

app_name = 'app'

urlpatterns = [
    # Categoria
    
    path('categoria/listar/', CategoriaListView.as_view(), name='categoria_listar'),
    path('categoria/crear/', CategoriaCreateView.as_view(), name='categoria_crear'),
    path('categoria/editar/<int:pk>/', CategoriaUpdateView.as_view(), name='categoria_editar'),
    path('categoria/eliminar/<int:pk>/', CategoriaDeleteView.as_view(), name='categoria_eliminar'), 

    # Ubicacion
    
    path('Ubicacion/listarU/', lista_ubicacion, name='ubicacion_listarU'),
    path('Ubicacion/crear/', UbicacionCreateView.as_view(), name='ubicacion_crear'),
    path('Ubicacion/editar/<int:pk>/', UbicacionUpdateView.as_view(), name='ubicacion_editar'),
    path('Ubicacion/eliminar/<int:pk>/', UbicacionDeleteView.as_view(), name='ubicacion_eliminar'),

    # Proveedor
    
    path('Proveedor/listarP/', lista_proveedor, name='proveedor_listarP'),
    path('Proveedor/crear/', ProveedorCreateView.as_view(), name='proveedor_crear'),
    path('Proveedor/editar/<int:pk>/', ProveedorUpdateView.as_view(), name='proveedor_editar'),
    path('Proveedor/eliminar/<int:pk>/', ProveedorDeleteView.as_view(), name='proveedor_eliminar'),

    #Cliente
    
    path('Cliente/listarC/', lista_cliente, name='cliente_listarC'),
    path('Cliente/crear/', ClienteCreateView.as_view(), name='cliente_crear'),
    path('Cliente/editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_editar'),
    path('Cliente/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_eliminar'),

]
