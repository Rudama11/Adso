from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from app.models import Proveedor
from app.forms import ProveedorForm

class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'Proveedor/listarP.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

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

@login_required
def lista_proveedor(request):
    context = {
        'titulo': 'Listado de Proveedores',
        'proveedores': Proveedor.objects.all(),
        'crear_url': reverse_lazy('app:proveedor_crear')
    }
    return render(request, 'Proveedor/listarP.html', context)
