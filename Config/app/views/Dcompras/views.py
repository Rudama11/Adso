import json
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from app.models import DetalleCompra, Producto, Compras, Stock
from app.forms import DetalleCompraForm , ComprasForm
from django.shortcuts import redirect
from django.db import transaction
from django.urls import reverse  
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
    
    def EliminarComprasD(request, id_compraD):
        comprad = DetalleCompra.objects.get(pk=id_compraD)
        comprad.delete()
        return redirect('app:detallecompra_listar')

class DetalleCompraCreateView(CreateView):
    model = DetalleCompra
    template_name = 'Compras/CompraD.html'
    form_class = DetalleCompraForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        compra_id = self.kwargs.get('compra_id')
        compra = get_object_or_404(Compras, id=compra_id)
        detalles_compra = DetalleCompra.objects.filter(compra=compra)

        context['form'] = ComprasForm(instance=compra)
        context['compra'] = compra
        context['detalles_compra'] = detalles_compra
        context['titulo'] = 'Detalles de Compra'
        context['listar_url'] = reverse_lazy('app:compras_listar')

        # Cargar productos
        context['productos'] = Producto.objects.all()  # Agrega esta línea para cargar los productos
        
        return context

    def form_valid(self, form):
        compra_id = self.kwargs['compra_id']
        form.instance.compra = get_object_or_404(Compras, id=compra_id)
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') != 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': 'Método no permitido'}, status=405)

        try:
            data = json.loads(request.body)

            # Verificar campos obligatorios
            required_keys = ['producto', 'cantidad', 'precio_unitario', 'iva', 'compra_id', 'num_factura']
            missing_keys = [key for key in required_keys if key not in data]
            if missing_keys:
                return JsonResponse({'success': False, 'error': f'Faltan campos requeridos: {", ".join(missing_keys)}.'}, status=400)

            # Obtener compra y producto
            compra = get_object_or_404(Compras, id=data['compra_id'])
            producto = get_object_or_404(Producto, id=data['producto'])

            cantidad = int(data['cantidad'])
            if cantidad <= 0:
                return JsonResponse({'success': False, 'error': 'La cantidad debe ser mayor que cero.'}, status=400)

            # Crear el detalle de compra
            with transaction.atomic():
                detalle_compra = DetalleCompra.objects.create(
                    producto=producto,
                    cantidad=cantidad,
                    precio_unitario=data['precio_unitario'],
                    iva=data['iva'],
                    compra=compra,
                    num_factura=data['num_factura']
                )

                # Actualizar o crear el stock del producto
                stock, created = Stock.objects.get_or_create(nombre_pro=producto)
                stock.cantidad += cantidad
                
                # Solo actualiza el precio si es nuevo o diferente
                if created or stock.precio != detalle_compra.precio_unitario:
                    stock.precio = detalle_compra.precio_unitario
                
                stock.save()

            # Enviar respuesta exitosa
            return JsonResponse({
                'success': True,
                'detalle_compra': detalle_compra.id,
                'message': 'Detalle de compra agregado correctamente.'
            })

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Error en los datos enviados.'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
# Vista para actualizar un detalle de compra existente
class DetalleCompraUpdateView(UpdateView):
    model = DetalleCompra
    form_class = DetalleCompraForm
    template_name = 'Dcompras/editar.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['compra_id'] = self.kwargs.get('compra_id')  # Pasa el ID de la compra si es necesario
        return kwargs

    def form_valid(self, form):
        num_factura = form.cleaned_data.get('num_factura')
        if not Compras.objects.filter(num_factura=num_factura).exists():
            form.add_error('num_factura', 'No existe una compra con el número de factura proporcionado.')
            return self.form_invalid(form)

        # Obtener la compra asociada al número de factura
        form.instance.compra = get_object_or_404(Compras, num_factura=num_factura)
        
        # Guardar el detalle de compra
        old_detalle = self.get_object()  # Obtiene el detalle de compra antes de la edición
        response = super().form_valid(form)
        
        # Actualizar el stock si la cantidad o el producto cambió
        self.actualizar_stock(form.instance, old_detalle)
        
        return response
    def get_success_url(self):
        return reverse_lazy('app:detallecompra_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Detalle de Compra'
        context['entidad'] = 'Detalle de Compra'
        context['listar_url'] = reverse_lazy('app:detallecompra_listar')
        return context


# Vista para obtener datos del producto en formato JSON
# def obtener_datos_producto(request):
#     producto_id = request.GET.get('producto_id')
#     try:
#         producto = Producto.objects.get(id=producto_id)
#         data = {
#             'precio_unitario': float(producto.precio_unitario),
#             'iva': float(producto.iva),
#         }
#         return JsonResponse(data)
#     except Producto.DoesNotExist:
#         return JsonResponse({'error': 'Producto no encontrado.'}, status=404)