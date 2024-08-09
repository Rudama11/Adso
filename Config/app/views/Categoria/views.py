from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from app.models import Categoria
from app.forms import CategoriaForm

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'Categoria/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data = {'Nombre': 'Lorena'}
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Categorías'
        context['entidad'] = 'Categoría'
        context['crear_url'] = reverse_lazy('app:categoria_crear')
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Obtener los parámetros GET
        nombre = self.request.GET.get('nombre')
        descripcion = self.request.GET.get('descripcion')

        # Aplicar filtros si los parámetros existen
        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        if descripcion:
            queryset = queryset.filter(descripcion__icontains=descripcion)

        return queryset
class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'Categoria/crear.html'
    success_url = reverse_lazy('app:categoria_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Categorías'
        context['entidad'] = 'Categoría'
        context['listar_url'] = reverse_lazy('app:categoria_listar')
        return context

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'Categoria/crear.html'
    success_url = reverse_lazy('app:categoria_listar')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Categoría'
        context['entidad'] = 'Categoría'
        context['listar_url'] = reverse_lazy('app:categoria_listar')
        return context

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'Categoria/eliminar.html'
    success_url = reverse_lazy('app:categoria_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Categoría'
        context['entidad'] = 'Categoría'
        context['listar_url'] = reverse_lazy('app:categoria_listar')
        return context