from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from app.models import DetalleCompra, Producto, Compras
from app.forms import DetalleCompraForm

# Vista para listar detalles de compra
class DetalleCompraListView(ListView):
    model = DetalleCompra
    template_name = 'Dcompras/listar.html'
    
    @method_decorator(login_required)  # Requiere autenticación para acceder
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        """
        Agrega datos adicionales al contexto de la plantilla.
        """
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Detalles de Compras'
        context['entidad'] = 'Detalle de Compra'
        context['crear_url'] = reverse_lazy('app:detallecompra_crear')  # URL para crear un nuevo detalle
        context['request'] = self.request  # Incluye la solicitud en el contexto
        return context

# Vista para crear un nuevo detalle de compra
class DetalleCompraCreateView(CreateView):
    model = DetalleCompra
    form_class = DetalleCompraForm
    template_name = 'Dcompras/crear.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['compra_id'] = self.kwargs.get('compra_id')
        return kwargs

    def form_valid(self, form):
        num_factura = form.cleaned_data.get('num_factura')
        if not Compras.objects.filter(num_factura=num_factura).exists():
            form.add_error('num_factura', 'No existe una compra con el número de factura proporcionado.')
            return self.form_invalid(form)
        form.instance.compra = get_object_or_404(Compras, num_factura=num_factura)
        return super().form_valid(form)

    def get_success_url(self):
        # Redirige a la vista de lista de detalles de compra
        return reverse_lazy('app:detallecompra_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Detalle de Compra'
        context['entidad'] = 'Detalle de Compra'
        context['listar_url'] = reverse_lazy('app:detallecompra_listar')
        return context

# Vista para actualizar un detalle de compra existente
class DetalleCompraUpdateView(UpdateView):
    model = DetalleCompra
    form_class = DetalleCompraForm
    template_name = 'Dcompras/editar.html'
    success_url = reverse_lazy('app:detallecompra_listar')  # URL para redirigir tras la actualización
    
    def get_context_data(self, **kwargs):
        """
        Agrega datos adicionales al contexto de la plantilla para la actualización de un detalle.
        """
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Detalle de Compra'
        context['entidad'] = 'Detalle de Compra'
        context['listar_url'] = reverse_lazy('app:detallecompra_listar')  # URL para listar los detalles
        return context

# Vista para eliminar un detalle de compra
class DetalleCompraDeleteView(DeleteView):
    model = DetalleCompra
    template_name = 'Dcompras/eliminar.html'
    success_url = reverse_lazy('app:detallecompra_listar')  # URL para redirigir tras la eliminación

    def get_context_data(self, **kwargs):
        """
        Agrega datos adicionales al contexto de la plantilla para la eliminación de un detalle.
        """
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Detalle de Compra'
        context['entidad'] = 'Detalle de Compra'
        context['listar_url'] = reverse_lazy('app:detallecompra_listar')  # URL para listar los detalles
        return context

# Vista para obtener datos del producto en formato JSON
def obtener_datos_producto(request):
    producto_id = request.GET.get('producto_id')
    try:
        producto = Producto.objects.get(id=producto_id)
        data = {
            'precio_unitario': float(producto.precio_unitario),
            'iva': float(producto.iva),
        }
        return JsonResponse(data)
    except Producto.DoesNotExist:
        return JsonResponse({'error': 'Producto no encontrado.'}, status=404)