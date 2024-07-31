from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from typing import Any
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.http.response import HttpResponse as HttpResponse
from app.models import Proveedor
from app.forms import ProveedorForm

@login_required
def lista_proveedor(request):
    context = {
        'titulo': 'Listado de Proveedores',
        'proveedores': Proveedor.objects.all(),
        'crear_url': reverse_lazy('app:proveedor_crear')  # Asegúrate de tener esta línea
    }
    return render(request, 'Proveedor/listarP.html', context)

class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'Proveedor/listarP.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data = {'Nombre': 'Lorena'}
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Proveedores'
        context['entidad'] = 'Proveedor'
        context['crear_url'] = reverse_lazy('app:proveedor_crear')
        return context

class ProveedorCreateView(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'Proveedor/crearP.html'
    success_url = reverse_lazy('app:proveedor_listarP')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Proveedor'
        context['entidad'] = 'Proveedor'
        context['listar_url'] = reverse_lazy('app:proveedor_listarP')
        return context

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'Proveedor/crearP.html'
    success_url = reverse_lazy('app:proveedor_listarP')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Proveedor'
        context['entidad'] = 'Proveedor'
        context['listar_url'] = reverse_lazy('app:proveedor_listarP')
        return context

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'Proveedor/eliminarP.html'
    success_url = reverse_lazy('app:proveedor_listarP')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Proveedor'
        context['entidad'] = 'Proveedor'
        context['listar_url'] = reverse_lazy('app:proveedor_listarP')
        return context
