from django.http import JsonResponse, HttpResponseBadRequest
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from app.models import Venta, Cliente,  DetalleVenta
from app.forms import VentaForm,VentaEditForm
from django.utils.dateparse import parse_date
from app.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import get_object_or_404, redirect

# Vista para listar ventas
class VentasListView(LoginRequiredMixin,ListView):
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
         # Agregar breadcrumbs
        context['breadcrumbs'] = [
            {'nombre': 'Modulos', 'url': '/dashboard'},
            {'nombre': 'Ventas', 'url': reverse_lazy('app:venta_listar')},
        ]
        return context
    
    
    
# Vista para crear una nueva venta
class VentasCreateView(LoginRequiredMixin, CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'Ventas/crear.html'
    success_url = reverse_lazy('app:venta_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.all()  
        context['titulo'] = 'Crear Venta'
        context['entidad'] = 'Venta'
        context['listar_url'] = self.success_url  
           # Agregar breadcrumbs
        context['breadcrumbs'] = [
            {'nombre': 'Modulos', 'url': '/dashboard'},
            {'nombre': 'Ventas', 'url': reverse_lazy('app:venta_listar')},
            {'nombre': 'Crear Ventas', 'url': reverse_lazy('app:venta_crear')},
        ]
        
        return context

    def form_valid(self, form):
        # Crear la instancia de Venta, pero no guardar aún
        venta = form.save(commit=False)
        
        # Establecer valores predeterminados para total_venta y estado
        venta.estado = 'editable'  # O el valor que desees establecer

        # Guardar la venta
        venta.save()
        
        return JsonResponse({
            'success': True,
            'message': 'Venta creada exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)

def cambiar_estado_venta(request, venta_id):
    # Obtener la venta
    venta = get_object_or_404(Venta, id=venta_id)
    
    # Cambiar el estado de "editable" a "bloqueado" y viceversa
    if venta.estado == 'editable':
        venta.estado = 'bloqueado'
    else:
        venta.estado = 'editable'
    
    # Guardar el cambio en la base de datos
    venta.save()
    
    # Redirigir a la lista de ventas o a donde prefieras
    return redirect('app:venta_listar')  # Asumiendo que tienes una vista llamada 'lista_ventas'

# Vista para actualizar una venta existente
class VentasUpdateView(LoginRequiredMixin, UpdateView):
    model = Venta
    form_class = VentaEditForm
    template_name = 'Ventas/editarVen.html'
    success_url = reverse_lazy('app:venta_listar')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Venta'
        context['entidad'] = 'Ventas'
        context['listar_url'] = reverse_lazy('app:venta_listar')  
         # Añadir breadcrumbs
        context['breadcrumbs'] = [
            {'nombre': 'Modulos', 'url': '/dashboard'},
            {'nombre': 'Ventas', 'url': reverse_lazy('app:venta_listar')},
            {'nombre': 'Editar Ventas', 'url': reverse_lazy('app:venta_editar', args=[self.object.pk])},
        ]

        return context

    
    def form_valid(self, form):
        # Guardar el formulario como está, ya que la validación se realiza en el formulario
        form.save()  # Guarda el objeto

        return JsonResponse({
            'success': True,
            'message': 'Factura actualizada correctamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)

