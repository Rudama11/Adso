from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.urls import reverse_lazy
from app.models import Proveedor
from app.forms import ProveedorForm
from django.contrib import messages
from django.views.generic import UpdateView
from app.choices import Tipo_Documento_Choices, Tipo_Persona_Choices  # Importa tus choices
from django.shortcuts import redirect

@login_required
def lista_proveedor(request):
    context = {
        'titulo': 'Listado de Proveedores',
        'crear_url': reverse_lazy('app:proveedor_crear'),
        'tipo_documento_choices': Tipo_Documento_Choices,  # Añade los choices aquí
        'tipo_persona_choices': Tipo_Persona_Choices  # Añade los choices aquí
    }
    
    # Filtrado basado en parámetros GET
    proveedores = Proveedor.objects.all()
    filtros = {
        'tipo_persona': 'tipo_persona',
        'nombres__icontains': 'nombres',
        'razon_social__icontains': 'razon_social',
        'tipo_documento': 'tipo_documento',
        'numero_documento__icontains': 'numero_documento',
        'correo__icontains': 'correo',
        'telefono__icontains': 'telefono',
        'ciudad__icontains': 'ciudad',
        'direccion__icontains': 'direccion'
    }

    for filtro, parametro in filtros.items():
        valor = request.GET.get(parametro)
        if valor:
            proveedores = proveedores.filter(**{filtro: valor})

    context['proveedores'] = proveedores
    return render(request, 'Proveedor/listar.html', context)

class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'Proveedor/listar.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'titulo': 'Listado de Proveedores',
            'entidad': 'Proveedor',
            'crear_url': reverse_lazy('app:proveedor_crear'),
            'tipo_documento_choices': Tipo_Documento_Choices,
            'tipo_persona_choices': Tipo_Persona_Choices
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        filtros = {
            'tipo_persona': 'tipo_persona',
            'nombres__icontains': 'nombres',
            'razon_social__icontains': 'razon_social',
            'tipo_documento': 'tipo_documento',
            'numero_documento__icontains': 'numero_documento',
            'correo__icontains': 'correo',
            'telefono__icontains': 'telefono',
            'ciudad__icontains': 'ciudad',
            'direccion__icontains': 'direccion'
        }

        for filtro, parametro in filtros.items():
            valor = self.request.GET.get(parametro)
            if valor:
                queryset = queryset.filter(**{filtro: valor})

        return queryset
    
    def EliminarProveedor(request, id_prove):
        prove = Proveedor.objects.get(pk=id_prove)
        prove.delete()
        return redirect('app:proveedor_listar')
    

class ProveedorCreateView(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'Proveedor/crear.html'
    success_url = reverse_lazy('app:proveedor_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'titulo': 'Crear Proveedor',
            'entidad': 'Proveedor',
            'listar_url': reverse_lazy('app:proveedor_listar')
        })
        return context

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'Proveedor/editarProv.html'
    success_url = reverse_lazy('app:proveedor_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'titulo': 'Actualizar Proveedor',
            'entidad': 'Proveedor',
            'listar_url': reverse_lazy('app:proveedor_listar')
        })
        return context
    
class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'Proveedor/eliminar.html'
    success_url = reverse_lazy('app:proveedor_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'titulo': 'Eliminar Proveedor',
            'entidad': 'Proveedor',
            'listar_url': reverse_lazy('app:proveedor_listar')
        })
        return context