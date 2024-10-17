from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from app.models import Producto, Categoria, Tipo
from app.forms import ProductoForm, ProductoFilterForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_POST
from app.mixins import LoginRequiredMixin

class ProductoListView(LoginRequiredMixin,ListView):
    model = Producto
    template_name = 'Producto/listar.html'
    context_object_name = 'productos'

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
    
    @require_POST
    @user_passes_test(lambda u: u.is_superuser or u.is_staff)
    def EliminarProducto(request, id_producto):
        try:
            producto = get_object_or_404(Producto, pk=id_producto)
            producto.delete()
            return JsonResponse({'status': 'success', 'message': 'Categoría eliminada correctamente'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Productos'
        context['entidad'] = 'Producto'
        context['crear_url'] = reverse_lazy('app:producto_crear')

        context['categorias'] = Categoria.objects.all()
        context['tipos'] = Tipo.objects.all()
        context['form'] = ProductoFilterForm(self.request.GET)

         # Agregar breadcrumbs
        context['breadcrumbs'] = [
            {'nombre': 'Modulos', 'url': '/dashboard'},
            {'nombre': 'Productos', 'url': reverse_lazy('app:producto_listar')},
        ]
        return context
    
class ProductoCreateView(LoginRequiredMixin,CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Producto/crear.html'
    success_url = reverse_lazy('producto_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Producto'
        context['entidad'] = 'Producto'
        context['listar_url'] = reverse_lazy('app:producto_listar')
         # Agregar breadcrumbs
        context['breadcrumbs'] = [
            {'nombre': 'Modulos', 'url': '/dashboard'},
            {'nombre': 'Productos', 'url': reverse_lazy('app:producto_listar')},
            {'nombre': 'Crear Producto', 'url': reverse_lazy('app:producto_crear')},
        ]
        
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

class ProductoUpdateView(LoginRequiredMixin,UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'Producto/editarP.html'
    success_url = reverse_lazy('app:producto_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Producto'
        context['entidad'] = 'Productos'
        context['listar_url'] = reverse_lazy('app:producto_listar')
         # Añadir breadcrumbs
        context['breadcrumbs'] = [
            {'nombre': 'Inicio', 'url': '/'},
            {'nombre': 'Categorías', 'url': reverse_lazy('app:producto_listar')},
            {'nombre': 'Editar', 'url': reverse_lazy('app:producto_editarP', args=[self.object.pk])},
        ]

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