from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.urls import reverse_lazy
from app.models import Venta, Producto, Cliente
from app.forms import VentaForm

class VentasListView(ListView):
    model = Venta
    template_name = 'Ventas/listarV.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        num_factura = self.request.GET.get('num_factura')
        fecha_emision = self.request.GET.get('fecha_emision')
        cliente = self.request.GET.get('cliente')
        persona = self.request.GET.get('persona')
        total = self.request.GET.get('total')
        
        if num_factura:
            queryset = queryset.filter(num_factura__icontains(num_factura))
        if fecha_emision:
            queryset = queryset.filter(fecha_emision=fecha_emision)
        if cliente:
            queryset = queryset.filter(cliente__nombre__icontains(cliente))
        if persona:
            queryset = queryset.filter(persona__nombre__icontains(persona))
        if total:
            queryset = queryset.filter(total__icontains(total))
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Ventas'
        context['entidad'] = 'Venta'
        context['crear_url'] = reverse_lazy('app:venta_crear')
        # Agregar los valores de las opciones de filtrado al contexto
        context['request'] = self.request
        return context

class VentasCreateView(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = 'Ventas/crearV.html'
    success_url = reverse_lazy('app:venta_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Venta'
        context['entidad'] = 'Venta'
        context['listar_url'] = reverse_lazy('app:venta_listar')
        return context

class VentasUpdateView(UpdateView):
    model = Venta
    form_class = VentaForm
    template_name = 'Ventas/crearV.html'
    success_url = reverse_lazy('app:venta_listar')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Venta'
        context['entidad'] = 'Venta'
        context['listar_url'] = reverse_lazy('app:venta_listar')
        return context

class VentasDeleteView(DeleteView):
    model = Venta
    template_name = 'Ventas/eliminarV.html'
    success_url = reverse_lazy('app:venta_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Venta'
        context['entidad'] = 'Venta'
        context['listar_url'] = reverse_lazy('app:venta_listar')
        return context