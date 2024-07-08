from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from app.models import Tipo
from app.forms import TipoForm

def lista_tipo(request):
    context = {
        'titulo': 'Listado de tipos de productos',
        'tipos': Tipo.objects.all()
    }
    return render(request, 'Tipo/listar.html', context)

class TipoListView(ListView):
    model = Tipo
    template_name = 'Tipo/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data = {'Nombre': 'Lorena'}
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de tipos de productos'
        context['entidad'] = 'Tipo'
        context['crear_url'] = reverse_lazy('app:tipo_crear')
        return context

class TipoCreateView(CreateView):
    model = Tipo
    form_class = TipoForm
    template_name = 'Tipo/crear.html'
    success_url = reverse_lazy('app:tipo_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear un tipo de producto'
        context['entidad'] = 'Tipo'
        context['listar_url'] = reverse_lazy('app:tipo_listar')
        return context

class TipoUpdateView(UpdateView):
    model = Tipo
    form_class = TipoForm
    template_name = 'Tipo/crear.html'
    success_url = reverse_lazy('app:tipo_listar')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar tipo de producto'
        context['entidad'] = 'Tipo'
        context['listar_url'] = reverse_lazy('app:tipo_listar')
        return context

class TipoDeleteView(DeleteView):
    model = Tipo
    template_name = 'Tipo/eliminar.html'
    success_url = reverse_lazy('app:tipo_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar un tipo de producto'
        context['entidad'] = 'Tipo'
        context['listar_url'] = reverse_lazy('app:tipo_listar')
        return context