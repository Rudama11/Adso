from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.urls import reverse_lazy
from app.models import Venta, Producto, Cliente , DetalleVenta
from app.forms import VentaForm
from django.utils.dateparse import parse_date

# Vista para listar ventas
class VentasListView(ListView):
    model = Venta
    template_name = 'ventas/listar.html'
    context_object_name = 'ventas'

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtrar por número de factura
        num_factura = self.request.GET.get('num_factura', None)
        if num_factura:
            queryset = queryset.filter(num_factura__icontains=num_factura)

        # Filtrar por fecha de emisión
        fecha_emision = self.request.GET.get('fecha_emision', None)
        if fecha_emision:
            # Usar parse_date para convertir el string a un objeto datetime.date
            fecha_emision = parse_date(fecha_emision)
            if fecha_emision:
                queryset = queryset.filter(fecha_emision=fecha_emision)

        # Filtrar por cliente
        cliente = self.request.GET.get('cliente', None)
        if cliente:
            queryset = queryset.filter(cliente__nombres__icontains=cliente)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Venta'
        context['entidad'] = 'Ventas'
        context['crear_url'] = reverse_lazy('app:venta_crear')  
        return context
    
    
# Vista para crear una nueva venta
class VentasCreateView(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'Ventas/crear.html'
    success_url = reverse_lazy('app:venta_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.all()  
        context['productos'] = Producto.objects.all()  
        context['titulo'] = 'Crear Venta'
        context['entidad'] = 'Venta'
        context['listar_url'] = reverse_lazy('app:venta_listar')  
        return context
    


# Vista para actualizar una venta existente
class VentasUpdateView(UpdateView):
    model = Venta
    form_class = VentaForm
    template_name = 'Ventas/editarVen.html'
    success_url = reverse_lazy('app:venta_listar')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Venta'
        context['entidad'] = 'Venta'
        context['listar_url'] = reverse_lazy('app:venta_listar')  
        return context

# Vista para eliminar una venta
class VentasDeleteView(DeleteView):
    model = Venta
    template_name = 'Ventas/eliminar.html'
    success_url = reverse_lazy('app:venta_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Venta'
        context['entidad'] = 'Venta'
        context['listar_url'] = reverse_lazy('app:venta_listar')  
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

def venta_detalle(request, id):
    venta = get_object_or_404(Venta, id=id)  # Buscar por id 
    detalles_venta = DetalleVenta.objects.filter(venta=venta)  # Filtra los detalles de la venta
    form = VentaForm(instance=venta)
    
    context = {
        'form': form,
        'titulo': 'Detalles de Venta',
        'listar_url': reverse_lazy('app:venta_listar'),
        'detalles_venta': detalles_venta,  # Pasamos los detalles de la venta al contexto
    }
    return render(request, 'Ventas/ventaD.html', context)

