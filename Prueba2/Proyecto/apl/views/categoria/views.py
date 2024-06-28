from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView, CreateView,UpdateView,DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render



from apl.models import Categoria
from apl.forms import CategoriaForm

def lista_categoria(request):

    nombre = {
        'titulo': 'Listado de Categorías',
        'categorias': Categoria.objects.all(),

    }
    return render(request, 'categoria/listar.html', nombre)

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria/listar.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Ruben Martinez'}
        return JsonResponse(nombre)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Categorías'
        context['crear_url'] = reverse_lazy('apl:categoria_crear')
        context['entidad'] = 'Categoría'
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
    template_name = 'categoria/editar.html'
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