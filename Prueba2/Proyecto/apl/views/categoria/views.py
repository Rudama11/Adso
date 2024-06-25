#from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import JsonResponse
from django.views.generic import ListView, CreateView
from django.utils.decorators import method_decorator
from django.shortcuts import render,redirect
from django.urls import reverse_lazy


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

    # @method_decorator(login_required)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        nombre = {'nombre': 'Ruben Martinez'}
        return JsonResponse(nombre)
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Categorías'
        return context

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'categoria/crear.html'
    success_url = reverse_lazy('apl:categoria_lista')