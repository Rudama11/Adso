from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse  # Importar JsonResponse
from app.forms import DetalleVentaForm
from app.models import DetalleVenta, Stock, Venta


# Listado de detalles de ventas
@method_decorator(login_required, name='dispatch')
class DetalleVentaListView(ListView):
    model = DetalleVenta
    template_name = 'Dventas/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Detalles de Ventas'
        context['entidad'] = 'Detalle de Venta'
        context['crear_url'] = reverse_lazy('app:detalleventa_crear')
        return context

# Crear un nuevo detalle de venta
@method_decorator(login_required, name='dispatch')
class DetalleVentaCreateView(CreateView):
    model = DetalleVenta
    form_class = DetalleVentaForm
    template_name = 'Dventas/crear.html'

    def form_valid(self, form):
        num_factura = form.cleaned_data.get('num_factura')
        if not Venta.objects.filter(num_factura=num_factura).exists():
            form.add_error('num_factura', 'No existe una venta con el número de factura proporcionado.')
            return self.form_invalid(form)

        # Asigna la instancia de venta al detalle de venta
        form.instance.venta = get_object_or_404(Venta, num_factura=num_factura)

        # Guarda el formulario primero para obtener la instancia de detalle_venta
        detalle_venta = form.save()

        # Llama al método para actualizar el stock
        self.actualizar_stock(detalle_venta)

        # Redirige a la vista de detalle de venta usando el ID de la venta
        return redirect(reverse('app:venta_detalle', kwargs={'id': detalle_venta.venta.id}))

    def actualizar_stock(self, detalle_venta):
        """
        Actualiza el stock basado en el detalle de venta.
        """
        stock = detalle_venta.producto  # Esto es correcto ya que detalle_venta.producto es Stock
        cantidad = detalle_venta.cantidad

        # Aquí verificamos que la cantidad en stock es suficiente
        if stock.cantidad >= cantidad:  # Verifica que hay suficiente stock
            stock.cantidad -= cantidad
            stock.save()
            print(f"Stock actualizado: {stock.nombre_pro.nombre} - Nueva cantidad: {stock.cantidad}")  # Debugging
        else:
            print(f"No hay suficiente stock para {stock.nombre_pro.nombre}. Stock actual: {stock.cantidad}, solicitado: {cantidad}")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Detalle de Venta'
        context['entidad'] = 'Detalle de Venta'
        context['listar_url'] = reverse_lazy('app:venta_detalle')  # Puedes cambiar esto si necesitas
        return context
# Actualizar un detalle de venta
@method_decorator(login_required, name='dispatch')
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

# Eliminar un detalle de venta
@method_decorator(login_required, name='dispatch')
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


def obtener_id_venta_por_factura(request):
    num_factura = request.GET.get('num_factura', None)
    if num_factura:
        try:
            venta = Venta.objects.get(num_factura=num_factura)
            return JsonResponse({'id_venta': venta.id})
        except Venta.DoesNotExist:
            return JsonResponse({'error': 'No se encontró ninguna venta con ese número de factura.'}, status=404)
    return JsonResponse({'error': 'Número de factura no proporcionado.'}, status=400)

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
