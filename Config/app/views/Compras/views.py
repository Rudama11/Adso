from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from app.models import Compras, Proveedor ,DetalleCompra
from app.forms import ComprasForm
from django.shortcuts import redirect

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
    
    def EliminarCompras(request, id_compra):
        compra = Compras.objects.get(pk=id_compra)
        compra.delete()
        return redirect('app:compra_listar')
    
    


class ComprasCreateView(CreateView):
    model = Compras
    form_class = ComprasForm
    template_name = 'Compras/crear.html'
    success_url = reverse_lazy('app:compras_listar')

    def form_valid(self, form):
        response = super().form_valid(form)
        num_factura = form.instance.num_factura
        self.object = form.instance
        context = self.get_context_data()
        context['num_factura'] = num_factura
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proveedores'] = Proveedor.objects.all()
        context['titulo'] = 'Crear Compra'
        context['entidad'] = 'Compras'
        context['listar_url'] = reverse_lazy('app:compras_listar')
        context['num_factura'] = self.object.num_factura if self.object else ''
        return context


class ComprasUpdateView(UpdateView):
    model = Compras
    form_class = ComprasForm
    template_name = 'Compras/editarCom.html'
    success_url = reverse_lazy('app:compras_listar')

    def get_object(self, queryset=None):
        return Compras.objects.get(num_factura=self.kwargs['num_factura'])

    def form_valid(self, form):
        response = super().form_valid(form)
        num_factura = form.instance.num_factura
        self.object = form.instance
        context = self.get_context_data()
        context['num_factura'] = num_factura
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Compra'
        context['entidad'] = 'Compras'
        context['listar_url'] = reverse_lazy('app:compras_listar')
        context['num_factura'] = self.object.num_factura if self.object else ''
        return context

class ComprasDeleteView(DeleteView):
    model = Compras
    template_name = 'Compras/eliminar.html'
    success_url = reverse_lazy('app:compras_listar')

    def get_object(self, queryset=None):
        return Compras.objects.get(num_factura=self.kwargs['num_factura'])

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