from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from app.models import DetalleCompra, Producto, Compras, Stock
from app.forms import DetalleCompraForm
from django.shortcuts import redirect

# Vista para listar detalles de compra
class DetalleCompraListView(ListView):
    model = DetalleCompra
    template_name = 'Dcompras/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Detalles de Compras'
        context['entidad'] = 'Detalle de Compra'
        context['crear_url'] = reverse_lazy('app:detallecompra_crear')
        context['request'] = self.request
        return context
    
    def EliminarDcompras(request, id_compra):
        compra = Dcompra.objects.get(pk=id_compra)
        compra.delete()
        return redirect('app:compra_listar')
    
    

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
        
        # Asignar la compra correspondiente al detalle
        form.instance.compra = get_object_or_404(Compras, num_factura=num_factura)
        
        # Guardar el detalle de compra
        response = super().form_valid(form)
        
        # Actualizar el stock después de guardar el detalle
        self.actualizar_stock(form.instance)
        
        return response

    def actualizar_stock(self, detalle_compra):
        """
        Actualiza el stock basado en el detalle de compra.
        """
        producto = detalle_compra.producto
        cantidad = detalle_compra.cantidad
        
        # Intentar obtener el producto en stock y actualizar la cantidad
        try:
            stock = Stock.objects.get(nombre_pro=producto)
            stock.cantidad += cantidad
            stock.save()
        except Stock.DoesNotExist:
            Stock.objects.create(nombre_pro=producto, cantidad=cantidad, precio=detalle_compra.precio_unitario)

    def get_success_url(self):
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
    success_url = reverse_lazy('app:detallecompra_listar')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Detalle de Compra'
        context['entidad'] = 'Detalle de Compra'
        context['listar_url'] = reverse_lazy('app:detallecompra_listar')
        return context

# Vista para eliminar un detalle de compra
class DetalleCompraDeleteView(DeleteView):
    model = DetalleCompra
    template_name = 'Dcompras/eliminar.html'
    success_url = reverse_lazy('app:detallecompra_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Detalle de Compra'
        context['entidad'] = 'Detalle de Compra'
        context['listar_url'] = reverse_lazy('app:detallecompra_listar')
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