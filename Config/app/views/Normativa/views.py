from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from app.models import Normativa
from app.forms import NormativaForm

def lista_Normativa(request):
    context = {
        'titulo': 'Lista de normas',
        'tipos': Normativa.objects.all()
    }
    return render(request, 'Normativa/listar.html', context)

class NormativaListView(ListView):
    model = Normativa
    template_name = 'normativa/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data = {'Nombre': 'Lorena'}
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Lista de normas'
        context['entidad'] = 'Normativa'
        context['crear_url'] = reverse_lazy('app:Normativa_crear')
        return context

class NormativaCreateView(CreateView):
    model = Normativa
    form_class = NormativaForm
    template_name = 'Normativa/crear.html'
    success_url = reverse_lazy('app:Normativa_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'añadir norma'
        context['entidad'] = 'Normativa'
        context['listar_url'] = reverse_lazy('app:Normativa_listar')
        return context

class NormativaUpdateView(UpdateView):
    model = Normativa
    form_class = NormativaForm
    template_name = 'Normativa/crear.html'
    success_url = reverse_lazy('app:Normativa_listar')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar norma'
        context['entidad'] = 'Normativa'
        context['listar_url'] = reverse_lazy('app:Normativa_listar')
        return context

class NormativaDeleteView(DeleteView):
    model = Normativa
    template_name = 'Normativa/eliminar.html'
    success_url = reverse_lazy('app:Normativa_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Norma'
        context['entidad'] = 'Normativa'
        context['listar_url'] = reverse_lazy('app:Normativa_listar')
        return context