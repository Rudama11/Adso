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
from app.views.Usuario.views import *
from app.views.Compras.views import *
from app.views.Stock.views import *

app_name = 'app'

urlpatterns = [

    #-------------------------------------------------- Categoría --------------------------------------------------
    
    path('Categoria/listar/', CategoriaListView.as_view(), name='categoria_listar'),
    path('Categoria/crear/', CategoriaCreateView.as_view(), name='categoria_crear'),
    path('Categoria/editar/<int:pk>/', CategoriaUpdateView.as_view(), name='categoria_editar'),
    path('Categoria/eliminar/<int:pk>/', CategoriaDeleteView.as_view(), name='categoria_eliminar'), 
    
    #-------------------------------------------------- Cliente ----------------------------------------------------
    
    path('Cliente/listarC/', ClienteListView.as_view(), name='cliente_listarC'),
    path('Cliente/crear/', ClienteCreateView.as_view(), name='cliente_crear'),
    path('Cliente/editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_editar'),
    path('Cliente/eliminar/<int:pk>/', ClienteDeleteView.as_view(), name='cliente_eliminar'),
    
    #-------------------------------------------------- Compras ----------------------------------------------------
    
    path('Compras/listar/', ComprasListView.as_view(), name='compras_listar'),
    path('Compras/crear/', ComprasCreateView.as_view(), name='compras_crear'),
    path('Compras/editar/<int:pk>/', ComprasUpdateView.as_view(), name='compras_editar'),
    path('Compras/eliminar/<int:pk>/', ComprasDeleteView.as_view(), name='compras_eliminar'),
    path('obtener-datos-proveedor/', obtener_datos_proveedor, name='obtener_datos_proveedor'),
    
    #-------------------------------------------------- Normativa -------------------------------------------------
    
    path('Normativa/listarN/', NormativaListView.as_view(), name='normativa_listar'),
    path('Normativa/crearN/', NormativaCreateView.as_view(), name='normativa_crear'),
    path('Normativa/editar/<int:pk>/', NormativaUpdateView.as_view(), name='normativa_editar'),
    path('Normativa/eliminar/<int:pk>/', NormativaDeleteView.as_view(), name='normativa_eliminar'),
    
    #-------------------------------------------------- Usuario ---------------------------------------------------
    
    path('Usuario/listar/', UsuarioListView.as_view(), name='usuario_listar'),
    path('Usuario/crear/', UsuarioCreateView.as_view(), name='usuario_crear'),
    path('Usuario/editar/<int:pk>/', UsuarioUpdateView.as_view(), name='usuario_editar'),
    path('Usuario/eliminar/<int:pk>/', UsuarioDeleteView.as_view(), name='usuario_eliminar'),
    
    #-------------------------------------------------- Producto --------------------------------------------------

    path('Producto/listar/', ProductoListView.as_view(), name='producto_listar'),
    path('Producto/crear/', ProductoCreateView.as_view(), name='producto_crear'),
    path('Producto/editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto_editar'),
    path('Producto/eliminar/<int:pk>/', ProductoDeleteView.as_view(), name='producto_eliminar'),
    
    #-------------------------------------------------- Proveedor --------------------------------------------------
    
    path('Proveedor/listarP/',ProveedorListView.as_view(), name='proveedor_listarP'),
    path('Proveedor/crear/', ProveedorCreateView.as_view(), name='proveedor_crear'),
    path('Proveedor/editar/<int:pk>/', ProveedorUpdateView.as_view(), name='proveedor_editar'),
    path('Proveedor/eliminar/<int:pk>/', ProveedorDeleteView.as_view(), name='proveedor_eliminar'),
    
    #-------------------------------------------------- Tipos de productos -----------------------------------------

    path('Tipo/listar/', TipoListView.as_view(), name='tipo_listar'),
    path('Tipo/crear/', TipoCreateView.as_view(), name='tipo_crear'),
    path('Tipo/editar/<int:pk>/', TipoUpdateView.as_view(), name='tipo_editar'),
    path('Tipo/eliminar/<int:pk>/', TipoDeleteView.as_view(), name='tipo_eliminar'),

    #-------------------------------------------------- Ubicación --------------------------------------------------
    
    path('Ubicacion/listarU/',UbicacionListView.as_view(), name='ubicacion_listarU'),
    path('Ubicacion/crear/', UbicacionCreateView.as_view(), name='ubicacion_crear'),
    path('Ubicacion/editar/<int:pk>/', UbicacionUpdateView.as_view(), name='ubicacion_editar'),
    path('Ubicacion/eliminar/<int:pk>/', UbicacionDeleteView.as_view(), name='ubicacion_eliminar'),
    path('municipios-por-departamento/', municipios_por_departamento, name='municipios_por_departamento'),

    #-------------------------------------------------- Ventas ----------------------------------------------------
    
    path('Ventas/listarV/', VentasListView.as_view(), name='venta_listar'),
    path('Ventas/crearV/', VentasCreateView.as_view(), name='venta_crear'),
    path('Ventas/editar/<int:pk>/', VentasUpdateView.as_view(), name='venta_editar'),
    path('Ventas/eliminar/<int:pk>/', VentasDeleteView.as_view(), name='venta_eliminar'),
    path('obtener-datos-cliente/', obtener_datos_cliente, name='obtener_datos_cliente'),
    path('obtener-datos-producto/', obtener_datos_producto, name='obtener_datos_producto'),

    #-------------------------------------------------- Backup del sistema ----------------------------------------
    
    path('backup/', backup_view, name='backup'),
    path('backup/create/', backup_database, name='respaldo'),
    path('backup/restore/', restore_database, name='restauracion'),

    #-------------------------------------------------- Stock ----------------------------------------
    
    path('Stock/listar',StockListView.as_view(), name='listar_stock'),
]