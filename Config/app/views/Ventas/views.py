from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.urls import reverse_lazy
from app.models import Venta, Producto, Cliente
from app.forms import VentaForm

# Vista para listar ventas
class VentasListView(ListView):
    model = Venta
    template_name = 'Ventas/listar.html'
    
    @method_decorator(login_required)  # Requiere autenticación para acceder
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        """
        Maneja las solicitudes POST. En este caso, devuelve datos estáticos en formato JSON.
        """
        data = {'Nombre': 'Lorena'}
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        """
        Agrega datos adicionales al contexto de la plantilla.
        """
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Ventas'
        context['entidad'] = 'Venta'
        context['crear_url'] = reverse_lazy('app:venta_crear')  # URL para crear una nueva venta
        context['request'] = self.request  # Incluye la solicitud en el contexto
        return context

# Vista para crear una nueva venta
class VentasCreateView(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'Ventas/crear.html'
    success_url = reverse_lazy('app:venta_listar')  # URL para redirigir tras la creación

    def get_context_data(self, **kwargs):
        """
        Agrega datos adicionales al contexto de la plantilla para la creación de una venta.
        """
        context = super().get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.all()  # Lista de todos los clientes
        context['productos'] = Producto.objects.all()  # Lista de todos los productos
        context['titulo'] = 'Crear Venta'
        context['entidad'] = 'Venta'
        context['listar_url'] = reverse_lazy('app:venta_listar')  # URL para listar las ventas
        return context

# Vista para actualizar una venta existente
class VentasUpdateView(UpdateView):
    model = Venta
    form_class = VentaForm
    template_name = 'Ventas/editarVen.html'
    success_url = reverse_lazy('app:venta_listar')  # URL para redirigir tras la actualización
    
    def get_context_data(self, **kwargs):
        """
        Agrega datos adicionales al contexto de la plantilla para la actualización de una venta.
        """
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Venta'
        context['entidad'] = 'Venta'
        context['listar_url'] = reverse_lazy('app:venta_listar')  # URL para listar las ventas
        return context

# Vista para eliminar una venta
class VentasDeleteView(DeleteView):
    model = Venta
    template_name = 'Ventas/eliminar.html'
    success_url = reverse_lazy('app:venta_listar')  # URL para redirigir tras la eliminación

    def get_context_data(self, **kwargs):
        """
        Agrega datos adicionales al contexto de la plantilla para la eliminación de una venta.
        """
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Venta'
        context['entidad'] = 'Venta'
        context['listar_url'] = reverse_lazy('app:venta_listar')  # URL para listar las ventas
        return context

# Vista para obtener datos del cliente en formato JSON
def obtener_datos_cliente(request):
    cliente_id = request.GET.get('cliente_id')
    try:
        cliente = Cliente.objects.get(id=cliente_id)
        data = {
            'nombre': cliente.nombres if cliente.tipo_persona == 'PN' else cliente.razon_social,
            'direccion': cliente.direccion,
            'correo': cliente.correo,
            'telefono': cliente.telefono,
        }
        return JsonResponse(data)
    except Cliente.DoesNotExist:
        return JsonResponse({'error': 'Cliente no encontrado.'}, status=404)

# Vista para obtener datos del producto en formato JSON
def obtener_datos_producto(request):
    producto_id = request.GET.get('producto_id')
    try:
        producto = Producto.objects.get(id=producto_id)
        data = {
            'precio': float(producto.precio),
        }
        return JsonResponse(data)
    except Producto.DoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado.'}, status=404)