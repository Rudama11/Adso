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
            descripcion = form.cleaned_data.get('descripcion')
            stock_min = form.cleaned_data.get('stock_min')
            stock_max = form.cleaned_data.get('stock_max')
            precio_min = form.cleaned_data.get('precio_min')
            precio_max = form.cleaned_data.get('precio_max')
            categoria = form.cleaned_data.get('categoria')
            tipo_pro = form.cleaned_data.get('tipo_pro')

            if nombre:
                queryset = queryset.filter(nombre__icontains=nombre)
            if descripcion:
                queryset = queryset.filter(descripcion__icontains=descripcion)
            if stock_min is not None:
                queryset = queryset.filter(stock__gte=stock_min)
            if stock_max is not None:
                queryset = queryset.filter(stock__lte=stock_max)
            if precio_min is not None:
                queryset = queryset.filter(precio__gte=precio_min)
            if precio_max is not None:
                queryset = queryset.filter(precio__lte=precio_max)
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

    def form_valid(self, form):
        # Guardar el objeto producto
        producto = form.save()

        # Retornar una respuesta JSON para que JavaScript lo maneje
        return JsonResponse({'status': 'success'})

    def form_invalid(self, form):
        # Si hay errores en el formulario, retornar los errores en formato JSON
        return JsonResponse({
            'status': 'error',
            'errors': form.errors,
        }, status=400)

    
class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Producto/editarP.html'
    success_url = reverse_lazy('app:producto_listar')

    def form_valid(self, form):
        # Puedes agregar lógica adicional si es necesario antes de guardar el formulario
        response = super().form_valid(form)
        return JsonResponse({'status': 'success'}, status=200)

    def form_invalid(self, form):
        # Si el formulario es inválido, puedes devolver los errores de los campos
        return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar un producto'
        context['entidad'] = 'Producto'
        context['listar_url'] = reverse_lazy('app:producto_listar')
        return context

