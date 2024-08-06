from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from app.models import Venta
from app.forms import VentaForm  # Cambiado a VentaForm

class VentasListView(ListView):
    model = Venta
    template_name = 'Ventas/listarV.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data = {'Nombre': 'Lorena'}
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Ventas'
        context['entidad'] = 'Venta'
        context['crear_url'] = reverse_lazy('app:venta_crear')
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

