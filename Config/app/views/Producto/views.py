from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.urls import reverse_lazy
from app.models import Producto, Categoria, Tipo
from app.forms import ProductoForm, ProductoFilterForm
from django.shortcuts import redirect
from django.http import JsonResponse

class ProductoListView(ListView):
    model = Producto
    template_name = 'Producto/listar.html'
    context_object_name = 'productos'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Crear instancia del formulario de filtrado con parámetros GET
        form = ProductoFilterForm(self.request.GET)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            categoria = form.cleaned_data.get('categoria')
            tipo_pro = form.cleaned_data.get('tipo_pro')

            if nombre:
                queryset = queryset.filter(nombre__icontains=nombre)
            if categoria:
                queryset = queryset.filter(categoria=categoria)
            if tipo_pro:
                queryset = queryset.filter(tipo_pro=tipo_pro)

        return queryset
    
    def EliminarProducto(request, id_producto):
        producto = Producto.objects.get(pk=id_producto)
        producto.delete()
        return redirect('app:producto_listar')
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Productos'
        context['entidad'] = 'Producto'
        context['crear_url'] = reverse_lazy('app:producto_crear')

        context['categorias'] = Categoria.objects.all()
        context['tipos'] = Tipo.objects.all()
        context['form'] = ProductoFilterForm(self.request.GET)

        return context
    
class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Producto/crear.html'
    success_url = reverse_lazy('producto_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Producto'
        context['entidad'] = 'Producto'
        context['listar_url'] = reverse_lazy('app:producto_listar')
        return context

    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Producto creado exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Producto/editarP.html'
    success_url = reverse_lazy('app:producto_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Producto'
        context['entidad'] = 'Productos'
        context['listar_url'] = reverse_lazy('app:producto_listar')
        return context

    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Producto actualizado exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)