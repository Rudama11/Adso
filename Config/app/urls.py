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
from app.views.Compras.views import *
from app.views.Stock.views import *
from app.views.Usuario.views import *
from app.views.Dcompras.views import *

app_name = 'app'

urlpatterns = [

    #-------------------------------------------------- Categoría --------------------------------------------------
    
    path('categoria/listar/', CategoriaListView.as_view(), name='categoria_listar'),
    path('categoria/crear/', CategoriaCreateView.as_view(), name='categoria_crear'),
    path('categoria/editar/<int:pk>/', CategoriaUpdateView.as_view(), name='categoria_editarC'),
    path('categoria/eliminar/<int:id_categ>/', CategoriaListView.eliminar_categoria, name='categoria_eliminar'), 
    
    #-------------------------------------------------- Cliente ----------------------------------------------------
    
    path('cliente/listar/', ClienteListView.as_view(), name='cliente_listar'),
    path('cliente/crear/', ClienteCreateView.as_view(), name='cliente_crear'),
    path('cliente/editar/<int:pk>/', ClienteUpdateView.as_view(), name='cliente_editarCli'),
    path('cliente/eliminar/<int:id_cliente>/', ClienteListView.EliminarCliente, name='cliente_eliminar'),
    
    #-------------------------------------------------- Compras ----------------------------------------------------
    
    path('compras/listar/', ComprasListView.as_view(), name='compras_listar'),
    path('compras/crear/', ComprasCreateView.as_view(), name='compras_crear'),
    path('compras/editar/<str:num_factura>/', ComprasUpdateView.as_view(), name='compras_editar'),
    path('compras/eliminar/<int:id_compra>/', ComprasListView.EliminarCompras, name='compras_eliminar'),
    path('compras/detalle/<str:num_factura>/', compra_detalle, name='compras_detalle'),
    path('obtener-datos-proveedor/', obtener_datos_proveedor, name='obtener_datos_proveedor'),
    
    #-------------------------------------------------- Normativa --------------------------------------------------
    
    path('normativa/listar/', NormativaListView.as_view(), name='normativa_listar'),
    path('normativa/crear/', NormativaCreateView.as_view(), name='normativa_crear'),
    path('normativa/editar/<int:pk>/', NormativaUpdateView.as_view(), name='normativa_editar'),
    path('normativa/eliminar/<int:id_norma>/', NormativaListView.EliminarNormativa, name='normativa_eliminar'),
    
    #-------------------------------------------------- Usuario ---------------------------------------------------
    
    path('usuario/listar/', UsuarioListView.as_view(), name='usuario_listar'),
    path('usuario/crear/', UsuarioCreateView.as_view(), name='usuario_crear'),
    path('usuario/editar/<int:pk>/', UsuarioUpdateView.as_view(), name='usuario_editar'),
    path('usuario/eliminar/<int:id_userc>/', UsuarioListView.EliminarUsuario, name='usuario_eliminar'),
    path('perfil/', perfil_view, name='perfil'),
    path('acceso-denegado/', acceso_denegado_view, name='acceso_denegado'),
    
    #-------------------------------------------------- Producto --------------------------------------------------

    path('producto/listar/', ProductoListView.as_view(), name='producto_listar'),
    path('producto/crear/', ProductoCreateView.as_view(), name='producto_crear'),
    path('producto/editar/<int:pk>/', ProductoUpdateView.as_view(), name='producto_editarP'),
    path('producto/eliminar/<int:id_producto>/', ProductoListView.EliminarProducto, name='producto_eliminar'),
    
    #-------------------------------------------------- Proveedor --------------------------------------------------
    
    path('proveedor/listar/', ProveedorListView.as_view(), name='proveedor_listar'),
    path('proveedor/crear/', ProveedorCreateView.as_view(), name='proveedor_crear'),
    path('proveedor/editar/<int:pk>/', ProveedorUpdateView.as_view(), name='proveedor_editar'),
    path('proveedor/eliminar/<int:id_prove>/', ProveedorListView.EliminarProveedor, name='proveedor_eliminar'),
    
    #-------------------------------------------------- Tipos de productos -----------------------------------------

    path('tipo/listar/', TipoListView.as_view(), name='tipo_listar'),
    path('tipo/crear/', TipoCreateView.as_view(), name='tipo_crear'),
    path('tipo/editar/<int:pk>/', TipoUpdateView.as_view(), name='tipo_editarTP'),
    path('tipo/eliminar/<int:id_tipo>/', TipoListView.EliminarTipo, name='tipo_eliminar'),

    #-------------------------------------------------- Ubicación --------------------------------------------------
    
    path('ubicacion/listar/', UbicacionListView.as_view(), name='ubicacion_listar'),
    path('ubicacion/crear/', UbicacionCreateView.as_view(), name='ubicacion_crear'),
    path('ubicacion/editar/<int:pk>/', UbicacionUpdateView.as_view(), name='ubicacion_editar'),
    path('ubicacion/eliminar/<int:id_ubica>/', UbicacionListView.EliminarUbicacion, name='ubicacion_eliminar'),
    path('municipios-por-departamento/', municipios_por_departamento, name='municipios_por_departamento'),

    #-------------------------------------------------- Ventas ----------------------------------------------------
    
    path('ventas/listar/', VentasListView.as_view(), name='venta_listar'),
    path('ventas/crear/', VentasCreateView.as_view(), name='venta_crear'),
    path('ventas/editar/<int:pk>/', VentasUpdateView.as_view(), name='venta_editar'),
    path('ventas/eliminar/<int:pk>/', VentasDeleteView.as_view(), name='venta_eliminar'),
    path('obtener-datos-cliente/', obtener_datos_cliente, name='obtener_datos_cliente'),
    path('obtener-datos-producto/', obtener_datos_producto, name='obtener_datos_producto'),

    #-------------------------------------------------- Backup del sistema ----------------------------------------
    
    path('backup/', backup_view, name='backup'),
    path('backup/create/', backup_database, name='respaldo'),
    path('backup/restore/', restore_database, name='restauracion'),

    #-------------------------------------------------- Stock -----------------------------------------------------
    
    path('stock/listar/', StockListView.as_view(), name='listar_stock'),

    #-------------------------------------------------- Dcompras --------------------------------------------------------
    
    path('detalle-compras/listar/', DetalleCompraListView.as_view(), name='detallecompra_listar'),
    path('detalle-compras/crear/', DetalleCompraCreateView.as_view(), name='detallecompra_crear'),
    path('detalle-compras/editar/<int:pk>/', DetalleCompraUpdateView.as_view(), name='detallecompra_editar'),
    path('detalle-compras/eliminar/<int:id_compraD>/', DetalleCompraListView.EliminarComprasD,name='detallecompra_eliminar'),
    path('obtener-datos-producto/', obtener_datos_producto, name='obtener_datos_producto'),
    path('detalle-compras/crear/<str:num_factura>/', DetalleCompraCreateView.as_view(), name='detallecompra_crear'),
]
