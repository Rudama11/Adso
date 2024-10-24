from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from app.models import Categoria
from app.forms import CategoriaForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_POST
from app.mixins import LoginRequired

class CategoriaListView(LoginRequired,ListView):
    model = Categoria
    template_name = 'Categoria/listar.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Categorías'
        context['entidad'] = 'Categoría'
        context['crear_url'] = reverse_lazy('app:categoria_crear')
        # Agregar breadcrumbs
        context['breadcrumbs'] = [
            {'nombre': 'Modulos', 'url': '/dashboard'},
            {'nombre': 'Categorías', 'url': reverse_lazy('app:categoria_listar')},
        ]
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()

        nombre = self.request.GET.get('nombre')
        descripcion = self.request.GET.get('descripcion')

        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        if descripcion:
            queryset = queryset.filter(descripcion__icontains=descripcion)

        return queryset

    @require_POST
    @user_passes_test(lambda u: u.is_superuser or u.is_staff)
    def eliminar_categoria(request, id_categ):
        try:
            categ = get_object_or_404(Categoria, pk=id_categ)
            categ.delete()
            return JsonResponse({'status': 'success', 'message': 'Categoría eliminada correctamente'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
        
class CategoriaCreateView(LoginRequired,CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'Categoria/crear.html'
    success_url = reverse_lazy('app:categoria_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Categoría'
        context['entidad'] = 'Categoría'
        context['listar_url'] = reverse_lazy('app:categoria_listar')
        # Agregar breadcrumbs
        context['breadcrumbs'] = [
            {'nombre': 'Modulos', 'url': '/dashboard'},
            {'nombre': 'Categorías', 'url': reverse_lazy('app:categoria_listar')},
            {'nombre': 'Crear Categoría', 'url': reverse_lazy('app:categoria_crear')},
        ]
        
        return context

    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Categoria creada exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)


class CategoriaUpdateView(LoginRequired,UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'Categoria/editarC.html'
    success_url = reverse_lazy('app:categoria_listar')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Categoría'
        context['entidad'] = 'Categoría'
        context['listar_url'] = reverse_lazy('app:categoria_listar')
        # Añadir breadcrumbs
        context['breadcrumbs'] = [
            {'nombre': 'Modulos', 'url': '/dashboard'},
            {'nombre': 'Categorías', 'url': reverse_lazy('app:categoria_listar')},
            {'nombre': 'Editar Categoría', 'url': reverse_lazy('app:categoria_editarC', args=[self.object.pk])},
        ]

        return context

    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Categoria actualizada exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)