from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from app.models import Compras, Proveedor
from app.forms import ComprasForm
from decimal import Decimal

class ComprasListView(ListView):
    model = Compras
    template_name = 'Compras/listar.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {'Nombre': 'Admin'}
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Compras'
        context['entidad'] = 'Compras'
        context['crear_url'] = reverse_lazy('app:compras_crear')
        context['request'] = self.request
        return context

class ComprasCreateView(CreateView):
    model = Compras
    form_class = ComprasForm
    template_name = 'Compras/crear.html'
    success_url = reverse_lazy('app:compras_listar')

    def form_valid(self, form):
        # Convertir los valores a Decimal para realizar las operaciones
        cantidad = form.cleaned_data.get('cantidad', Decimal(0))
        precio = form.cleaned_data.get('precio', Decimal(0))
        iva = form.cleaned_data.get('iva', Decimal(0))

        # Calcular el total utilizando Decimal
        total = (precio * cantidad) * (1 + iva / Decimal(100))

        # Asignar el valor calculado al campo 'total'
        form.instance.total = total
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proveedores'] = Proveedor.objects.all()
        context['titulo'] = 'Crear Compra'
        context['entidad'] = 'Compras'
        context['listar_url'] = reverse_lazy('app:compras_listar')
        return context


class ComprasUpdateView(UpdateView):
    model = Compras
    form_class = ComprasForm
    template_name = 'Compras/editarCom.html'
    success_url = reverse_lazy('app:compras_listar')

    def form_valid(self, form):
        # Convertir los valores a Decimal para realizar las operaciones
        cantidad = form.cleaned_data.get('cantidad', Decimal(0))
        precio = form.cleaned_data.get('precio', Decimal(0))
        iva = form.cleaned_data.get('iva', Decimal(0))

        # Calcular el total utilizando Decimal
        total = (precio * cantidad) * (1 + iva / Decimal(100))

        # Asignar el valor calculado al campo 'total'
        form.instance.total = total
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Compra'
        context['entidad'] = 'Compras'
        context['listar_url'] = reverse_lazy('app:compras_listar')
        return context


class ComprasDeleteView(DeleteView):
    model = Compras
    template_name = 'Compras/eliminar.html'
    success_url = reverse_lazy('app:compras_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Compra'
        context['entidad'] = 'Compras'
        context['listar_url'] = reverse_lazy('app:compras_listar')
        return context


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