from django.urls import path
from app.views.backup.views import *
from app.views.Categoria.views import *
from app.views.Ubicacion.views import *
from app.views.Proveedor.views import * 
from app.views.Cliente.views import *
from app.views.Tipo.views import *
from app.views.Producto.views import *
from app.views.Normativa.views import *
from app.views.Ventas.views import *
from app.views.Persona.views import *

app_name = 'app'

urlpatterns = [

    #-------------------------------------------------- Categoría --------------------------------------------------
    
    path('Categoria/listar/', CategoriaListView.as_view(), name='categoria_listar'),
    path('Categoria/crear/', CategoriaCreateView.as_view(), name='categoria_crear'),
    path('Categoria/editar/<int:pk>/', CategoriaUpdateView.as_view(), name='categoria_editar'),
    path('Categoria/eliminar/<int:pk>/', CategoriaDeleteView.as_view(), name='categoria_eliminar'), 

    #-------------------------------------------------- Ubicación --------------------------------------------------
    
    path('Ubicacion/listarU/', UbicacionListView.as_view(), name='ubicacion_listarU'),
    path('Ubicacion/crear/', UbicacionCreateView.as_view(), name='ubicacion_crear'),
    path('Ubicacion/editar/<int:pk>/', UbicacionUpdateView.as_view(), name='ubicacion_editar'),
    path('Ubicacion/eliminar/<int:pk>/', UbicacionDeleteView.as_view(), name='ubicacion_eliminar'),

    #-------------------------------------------------- Proveedor --------------------------------------------------
    
    path('Proveedor/listarP/',ProveedorListView.as_view(), name='proveedor_listarP'),
    path('Proveedor/crear/', ProveedorCreateView.as_view(), name='proveedor_crear'),
    path('Proveedor/editar/<int:pk>/', ProveedorUpdateView.as_view(), name='proveedor_editar'),
    path('Proveedor/eliminar/<int:pk>/', ProveedorDeleteView.as_view(), name='proveedor_eliminar'),

    #-------------------------------------------------- Cliente --------------------------------------------------
    
    path('Cliente/listarC/', ClienteListView.as_view(), name='cliente_listarC'),
    path('Cliente/crear/', ClienteCreateView.as_view(), name='cliente_crear'),
    path('Cliente/editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_editar'),
    path('Cliente/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_eliminar'),

    #-------------------------------------------------- Tipos de productos --------------------------------------------------

    path('Tipo/listar/', TipoListView.as_view(), name='tipo_listar'),
    path('Tipo/crear/', TipoCreateView.as_view(), name='tipo_crear'),
    path('Tipo/editar/<int:pk>/', TipoUpdateView.as_view(), name='tipo_editar'),
    path('Tipo/eliminar/<int:pk>/', TipoDeleteView.as_view(), name='tipo_eliminar'),

    #-------------------------------------------------- Producto --------------------------------------------------

    path('Producto/listar/', ProductoListView.as_view(), name='producto_listar'),
    path('Producto/crear/', ProductoCreateView.as_view(), name='producto_crear'),
    path('Producto/editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto_editar'),
    path('Producto/eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='producto_eliminar'),

    #-------------------------------------------------- Normativa --------------------------------------------------
    
    path('Normativa/listarN/', NormativaListView.as_view(), name='normativa_listar'),
    path('Normativa/crearN/', NormativaCreateView.as_view(), name='normativa_crear'),
    path('Normativa/editar/<int:pk>/', NormativaUpdateView.as_view(), name='normativa_editar'),
    path('Normativa/eliminar/<int:pk>/', NormativaDeleteView.as_view(), name='normativa_eliminar'),
    
    #-------------------------------------------------- Ventas --------------------------------------------------
    
    path('Ventas/listarV/', VentasListView.as_view(), name='venta_listar'),
    path('Ventas/crearV/', VentasCreateView.as_view(), name='venta_crear'),
    path('Ventas/editar/<int:pk>/', VentasUpdateView.as_view(), name='venta_editar'),
    path('Ventas/eliminar/<int:pk>/', VentasDeleteView.as_view(), name='venta_eliminar'),
    path('api/cliente/<int:id>/', cliente_api, name='cliente_api'),
    path('api/producto/<int:id>/', producto_api, name='producto_api'),

    #-------------------------------------------------- Persona --------------------------------------------------
    
    path('Persona/listar/', PersonaListView.as_view(), name='persona_listar'),
    path('Persona/crear/', PersonaCreateView.as_view(), name='persona_crear'),
    path('Persona/editar/<int:pk>/', PersonaUpdateView.as_view(), name='persona_editar'),
    path('Persona/eliminar/<int:pk>/', PersonaDeleteView.as_view(), name='persona_eliminar'),
    
    #-------------------------------------------------- Backup del sistema --------------------------------------------------
    
    path('backup/', backup_view, name='backup'),
    path('backup/create/', backup_database, name='respaldo'),
    path('backup/restore/', restore_database, name='restauracion')
]