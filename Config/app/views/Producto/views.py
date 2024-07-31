from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from app.models import Producto
from app.forms import ProductoForm

def lista_producto(request):
    context = {
        'titulo': 'Listado de Productos',
        'tipos': Producto.objects.all()
    }
    return render(request, 'Producto/listar.html', context)

class ProductoListView(ListView):
    model = Producto
    template_name = 'Producto/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data = {'Nombre': 'Lorena'}
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Productos'
        context['entidad'] = 'Producto'
        context['crear_url'] = reverse_lazy('app:producto_crear')
        return context

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Producto/crear.html'
    success_url = reverse_lazy('app:producto_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear un producto'
        context['entidad'] = 'Producto'
        context['listar_url'] = reverse_lazy('app:producto_listar')
        return context

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Producto/crear.html'
    success_url = reverse_lazy('app:producto_listar')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar un producto'
        context['entidad'] = 'Producto'
        context['listar_url'] = reverse_lazy('app:producto_listar')
        return context

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'Producto/eliminar.html'
    success_url = reverse_lazy('app:producto_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar un producto'
        context['entidad'] = 'Producto'
        context['listar_url'] = reverse_lazy('app:producto_listar')
        return context