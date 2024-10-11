from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.http import JsonResponse
from app.models import Compras, Proveedor ,DetalleCompra
from app.forms import ComprasForm
from django.shortcuts import get_object_or_404,render
from django.utils.dateparse import parse_date
from app.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class ComprasListView(LoginRequiredMixin,ListView):
    model = Compras
    template_name = 'Compras/listar.html'
    context_object_name = 'compras'

    def post(self, request, *args, **kwargs):
        data = {'Nombre': 'Admin'}
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Compras'
        context['entidad'] = 'Compras'
        context['crear_url'] = reverse_lazy('app:compras_crear')
        context['proveedores'] = Proveedor.objects.all()  # Añade la lista de proveedores al contexto
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        # Filtrar por número de factura
        num_factura = self.request.GET.get('num_factura', None)
        if num_factura:
            queryset = queryset.filter(num_factura__icontains=num_factura)

        # Filtrar por fecha de compra
        fecha_compra = self.request.GET.get('fecha_compra', None)
        if fecha_compra:
            # Usar parse_date para evitar problemas con la hora
            fecha_compra = parse_date(fecha_compra)
            if fecha_compra:
                queryset = queryset.filter(fecha_compra=fecha_compra)

        # Filtrar por proveedor
        proveedor_id = self.request.GET.get('proveedor', None)
        if proveedor_id:
            queryset = queryset.filter(proveedor__id=proveedor_id)  # Filtra por ID de proveedor

        return queryset
    
class ComprasCreateView(LoginRequiredMixin,CreateView):
    model = Compras
    form_class = ComprasForm
    template_name = 'Compras/crear.html'
    success_url = reverse_lazy('app:compras_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proveedores'] = Proveedor.objects.all()
        context['titulo'] = 'Crear Compra'
        context['entidad'] = 'Compras'
        context['listar_url'] = reverse_lazy('app:compras_listar')
        return context
    
    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Venta creada exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)

class ComprasUpdateView(LoginRequiredMixin,UpdateView):
    model = Compras
    form_class = ComprasForm
    template_name = 'Compras/editarCom.html'
    success_url = reverse_lazy('app:compras_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Compra'
        context['entidad'] = 'Compras'
        context['listar_url'] = reverse_lazy('app:compras_listar')
        return context
    
    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Venta creada exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)


def obtener_datos_proveedor(request):
    proveedor_id = request.GET.get('proveedor_id')
    try:
        proveedor = Proveedor.objects.get(id=proveedor_id)
        data = {
            'nombre': proveedor.nombres if proveedor.tipo_persona == 'PN' else proveedor.razon_social,
            'direccion': proveedor.direccion,
            'correo': proveedor.correo,
            'telefono': proveedor.telefono,
        }
        return JsonResponse(data)
    except Proveedor.DoesNotExist:
        return JsonResponse({'error': 'Proveedor no encontrado.'}, status=404)

@login_required
def compra_detalle(request, num_factura):
    compra = get_object_or_404(Compras, num_factura=num_factura)
    detalles_compra = DetalleCompra.objects.filter(compra=compra)
    form = ComprasForm(instance=compra)
    
    context = {
        'form': form,
        'titulo': 'Detalles de Compra',
        'listar_url': reverse_lazy('app:compras_listar'),
        'detalles_compra': detalles_compra,  # Pasamos los detalles de la compra al contexto
    }
    return render(request, 'Compras/CompraD.html', context)