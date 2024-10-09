from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json  
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
class VentaDetalleCreateView(CreateView): 
    model = DetalleVenta
    template_name = 'Ventas/VentaD.html'
    fields = ['producto', 'cantidad', 'precio', 'iva', 'total']  # Campos que se usarán en el formulario

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        venta = get_object_or_404(Venta, id=self.kwargs['venta_id'])  # Cambia 'id' a 'venta_id'
        context['venta'] = venta
        context['detalles_venta_url'] = reverse('app:detalle_venta', kwargs={'venta_id': venta.id})  # Cambia 'id' a 'venta_id' en el reverse
        context['detalles_venta'] = DetalleVenta.objects.filter(venta=venta)
        context['titulo'] = 'Detalles de Venta'
        context['listar_url'] = reverse('app:venta_listar')
        context['productos'] = Stock.objects.all()  # Obtener todos los productos
        return context

    def form_valid(self, form):
        # Asignar automáticamente el ID de venta y el número de factura
        form.instance.venta = get_object_or_404(Venta, id=self.kwargs['venta_id'])  # Cambia 'id' a 'venta_id'
        form.instance.num_factura = "Factura Generada"  # Cambia esto por la lógica necesaria para el número de factura
        
        # Calcular el total antes de guardar
        form.instance.total = form.instance.precio * form.instance.cantidad * (1 + (form.instance.iva / 100))
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') != 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': 'Método no permitido'}, status=405)
        
        try:
            data = json.loads(request.body)

            # Verificar campos obligatorios
            required_keys = ['producto', 'cantidad', 'precio', 'iva', 'id_venta']
            if any(key not in data for key in required_keys):
                return JsonResponse({'success': False, 'error': 'Faltan campos requeridos.'}, status=400)

            venta = get_object_or_404(Venta, id=data['id_venta'])
            producto = get_object_or_404(Stock, id=data['producto'])

            cantidad = int(data['cantidad'])
            if cantidad <= 0:
                return JsonResponse({'success': False, 'error': 'La cantidad debe ser mayor que cero.'}, status=400)

            # Crear y guardar el detalle de venta
            detalle_venta = DetalleVenta.objects.create(
                producto=producto,
                cantidad=cantidad,
                precio=data['precio'],
                iva=data['iva'],
                total=data['precio'] * cantidad * (1 + (data['iva'] / 100)),
                venta=venta,
                num_factura=data.get('num_factura', "Factura Generada")
            )

            # Actualizar stock después de crear el detalle de venta
            self.actualizar_stock(detalle_venta)

            return JsonResponse({'success': True, 'detalle_venta': detalle_venta.id})
        
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Error en los datos enviados.'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)

    def actualizar_stock(self, detalle_venta):
        stock = detalle_venta.producto
        cantidad = detalle_venta.cantidad
        # Actualizar el stock si hay suficiente cantidad
        if stock.cantidad >= cantidad:
            stock.cantidad -= cantidad
            stock.save()
        else:
            # Manejo de error si no hay suficiente stock
            raise ValueError(f"No hay suficiente stock para {stock.nombre_pro.nombre}. Stock actual: {stock.cantidad}, solicitado: {cantidad}")


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