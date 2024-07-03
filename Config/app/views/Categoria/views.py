from django.views.decorators.csrf import *
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import JsonResponse
from django.http.response import HttpResponse as HttpResponse
from django.urls import reverse_lazy

from app.models import Categoria
from app.forms import CategoriaForm

def lista_categoria(request):
    Nombre = {
        
    'titulo': 'Listado de Categorias',
    'categorias': Categoria.objects.all()
    }
    
    return render(request, 'categoria/listar.html', Nombre)

class CategoriaListView(ListView):
    model= Categoria
    template_name = 'categoria/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request,*args, **kwargs):
        Nombre ={'Nombre': 'Lorena'}
        return JsonResponse(Nombre)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Categorias'
        return context
    
class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/crear.html'
    success_url = reverse_lazy('apl:categoria_lista')

    def get_context(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Categorías'
        context['entidad'] = 'Categoría'
        context['listar_url'] = reverse_lazy('apl:categoria_lista')
        
        return context
    
class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/crear.html'
    success_url = reverse_lazy('apl:categoria_lista')
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Categoría'
        context['entidad'] = 'Categoría'
        context['listar_url'] = reverse_lazy('apl:categoria_lista')
        
        return context
    
class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categoria/eliminar.html'
    success_url = reverse_lazy('apl:categoria_lista')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Categoría'
        context['entidad'] = 'Categoría'
        context['listar_url'] = reverse_lazy('apl:categoria_lista')
        
        return context
