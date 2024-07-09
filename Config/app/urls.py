from django.urls import path
from app.views.Categoria.views import *
from app.views.Ubicacion.views import *
from app.views.Proveedor.views import * 
from app.views.Cliente.views import *
from app.views.Tipo.views import *
from app.views.Producto.views import *
from app.views.Normativa.views import *

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

    #Tipo

    path('Tipo/listar/', TipoListView.as_view(), name='tipo_listar'),
    path('Tipo/crear/', TipoCreateView.as_view(), name='tipo_crear'),
    path('Tipo/editar/<int:pk>/', TipoUpdateView.as_view(), name='tipo_editar'),
    path('Tipo/eliminar/<int:pk>/', TipoDeleteView.as_view(), name='tipo_eliminar'),

    # Producto

    path('Producto/listar/', ProductoListView.as_view(), name='producto_listar'),
    path('Producto/crear/', ProductoCreateView.as_view(), name='producto_crear'),
    path('Producto/editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto_editar'),
    path('Producto/eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='producto_eliminar'),
    
    # Norma
path('Normativa/listar/', NormativaListView.as_view(), name='Normativa_listar'),
    path('Normativa/crear/', NormativaCreateView.as_view(), name='Normativa_crear'),
    path('Normativa/editar/<int:pk>/', NormativaUpdateView.as_view(), name='Normativa_editar'),
    path('Normativa/eliminar/<int:pk>/', NormativaDeleteView.as_view(), name='Normativa_eliminar'),

]
