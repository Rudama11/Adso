from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.http import JsonResponse
from django.urls import reverse_lazy
from app.models import Compras,Proveedor
from app.forms import ComprasForm

# Vista para listar las compras
class ComprasListView(ListView):
    model = Compras
    template_name = 'Compras/listar.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # Asegura que el usuario esté autenticado antes de procesar la solicitud
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Maneja las solicitudes POST. En este caso, devuelve datos estáticos en formato JSON.
        """
        data = {'Nombre': 'Admin'}
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        """
        Agrega datos adicionales al contexto de la plantilla para la vista de listado de compras.
        """
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Compras'
        context['entidad'] = 'Compras'
        context['crear_url'] = reverse_lazy('app:compras_crear')
        context['request'] = self.request
        return context

# Vista para crear una nueva compra
class ComprasCreateView(CreateView):
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
        response = super().form_valid(form)
        print(form.cleaned_data)
        return response

# Vista para actualizar una compra existente
class ComprasUpdateView(UpdateView):
    model = Compras
    form_class = ComprasForm
    template_name = 'Compras/crear.html'
    success_url = reverse_lazy('app:compras_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Compra'
        context['entidad'] = 'Compras'
        context['listar_url'] = reverse_lazy('app:compras_listar')
        return context

# Vista para eliminar una compra existente
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

# Vista para obtener datos del proveedor en formato JSON
def obtener_datos_proveedor(request):
    proveedor_id = request.GET.get('proveedor_id')
    try:
        proveedor = Proveedor.objects.get(id=proveedor_id)
        # Retorna datos del proveedor según el tipo de persona
        data = {
            'nombre': proveedor.nombres if proveedor.tipo_persona == 'PN' else proveedor.razon_social,
            'direccion': proveedor.direccion,
            'correo': proveedor.correo,
            'telefono': proveedor.telefono,
        }
        return JsonResponse(data)
    except Proveedor.DoesNotExist:
        # Retorna un error si el proveedor no existe
        return JsonResponse({'error': 'Proveedor no encontrado.'}, status=404)