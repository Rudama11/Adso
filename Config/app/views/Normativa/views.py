from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from app.models import Normativa
from app.forms import NormativaForm

class NormativaListView(ListView):
    model = Normativa
    template_name = 'Normativa/listarN.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data = {'Nombre': 'Lorena'}
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de normativas'
        context['entidad'] = 'Normativas'
        context['crear_url'] = reverse_lazy('app:normativa_crear')
        return context

class NormativaCreateView(CreateView):
    model = Normativa
    form_class = NormativaForm
    template_name = 'Normativa/crearN.html'
    success_url = reverse_lazy('app:normativa_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear una normativa'
        context['entidad'] = 'Normativas'
        context['listar_url'] = reverse_lazy('app:normativa_listar')
        return context

class NormativaUpdateView(UpdateView):
    model = Normativa
    form_class = NormativaForm
    template_name = 'Normativa/crearN.html'
    success_url = reverse_lazy('app:normativa_listar')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar una Normativa'
        context['entidad'] = 'Normativa'
        context['listar_url'] = reverse_lazy('app:normativa_listar')
        return context

class NormativaDeleteView(DeleteView):
    model = Normativa
    template_name = 'Normativa/eliminarN.html'
    success_url = reverse_lazy('app:normativa_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar una Normativa'
        context['entidad'] = 'Normativas'
        context['listar_url'] = reverse_lazy('app:normativa_listar')
        return context