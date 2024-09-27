from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse  # Importar JsonResponse
from app.forms import DetalleVentaForm
from app.models import DetalleVenta, Stock, Venta

# Listado de detalles de ventas
class DetalleVentaListView(ListView):
    model = DetalleVenta
    template_name = 'Dventas/listar.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Detalles de Ventas'
        context['entidad'] = 'Detalle de Venta'
        context['crear_url'] = reverse_lazy('app:detalleventa_crear')
        return context

# Crear un nuevo detalle de venta
class DetalleVentaCreateView(CreateView):
    model = DetalleVenta
    form_class = DetalleVentaForm
    template_name = 'Dventas/crear.html'
    success_url = reverse_lazy('app:detalleventa_listar')

    def form_valid(self, form):
        num_factura = form.cleaned_data.get('num_factura')
        if not Venta.objects.filter(num_factura=num_factura).exists():
            form.add_error('num_factura', 'No existe una venta con el número de factura proporcionado.')
            return self.form_invalid(form)
        
        # Asignar la venta correspondiente al detalle
        form.instance.venta = get_object_or_404(Venta, num_factura=num_factura)
        
        # Guardar el detalle de venta
        response = super().form_valid(form)

        # Actualizar el stock solo si la venta es válida
        self.actualizar_stock(form.instance)  
        
        return response

    def actualizar_stock(self, detalle_venta):
        """
        Actualiza el stock basado en el detalle de venta.
        """
        producto = detalle_venta.producto
        cantidad = detalle_venta.cantidad
        
        try:
            stock = Stock.objects.get(nombre_pro=producto)
            stock.cantidad -= cantidad
            stock.save()
        except Stock.DoesNotExist:
            pass  # Manejar la excepción si es necesario

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Detalle de Venta'
        context['entidad'] = 'Detalle de Venta'
        context['listar_url'] = reverse_lazy('app:detalleventa_listar')
        return context

# Vista para actualizar un detalle de venta existente
class DetalleVentaUpdateView(UpdateView):
    model = DetalleVenta
    form_class = DetalleVentaForm
    template_name = 'Dventas/editar.html'
    success_url = reverse_lazy('app:detalleventa_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Detalle de Venta'
        context['entidad'] = 'Detalle de Venta'
        context['listar_url'] = reverse_lazy('app:detalleventa_listar')
        return context

# Vista para eliminar un detalle de venta
class DetalleVentaDeleteView(DeleteView):
    model = DetalleVenta
    template_name = 'Dventas/eliminar.html'
    success_url = reverse_lazy('app:detalleventa_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Detalle de Venta'
        context['entidad'] = 'Detalle de Venta'
        context['listar_url'] = reverse_lazy('app:detalleventa_listar')
        return context

# Vista para obtener datos del producto en formato JSON
def obtener_datos_producto(request):
    producto_id = request.GET.get('producto_id')
    try:
        # Obtén el producto desde el stock
        producto = Stock.objects.get(id=producto_id)
        data = {
            'precio_unitario': float(producto.precio),  # Asegúrate de que esto sea correcto
        }
        return JsonResponse(data)
    except Stock.DoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)  # Manejo general de errores


def obtener_id_venta_por_factura(request):
    num_factura = request.GET.get('num_factura', None)
    if num_factura:
        try:
            venta = Venta.objects.get(num_factura=num_factura)
            return JsonResponse({'id_venta': venta.id})
        except Venta.DoesNotExist:
            return JsonResponse({'error': 'No se encontró ninguna venta con ese número de factura.'}, status=404)
    return JsonResponse({'error': 'Número de factura no proporcionado.'}, status=400)