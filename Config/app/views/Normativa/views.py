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
    template_name = 'Normativa/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data = {'Nombre': 'Lorena'}
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Normativas'
        context['entidad'] = 'Normativas'
        context['crear_url'] = reverse_lazy('app:normativa_crear')
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        id = self.request.GET.get('id')
        decreto = self.request.GET.get('decreto')
        descripcion = self.request.GET.get('descripcion')
        producto = self.request.GET.get('producto')

        if id:
            queryset = queryset.filter(id=id)
        if decreto:
            queryset = queryset.filter(decreto__icontains=decreto)
        if descripcion:
            queryset = queryset.filter(descripcion__icontains=descripcion)
        if producto:
            queryset = queryset.filter(producto__icontains=producto)
        
        return queryset

class NormativaCreateView(CreateView):
    model = Normativa
    form_class = NormativaForm
    template_name = 'Normativa/crear.html'
    success_url = reverse_lazy('app:normativa_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear una Normativa'
        context['entidad'] = 'Normativas'
        context['listar_url'] = reverse_lazy('app:normativa_listar')
        return context

class NormativaUpdateView(UpdateView):
    model = Normativa
    form_class = NormativaForm
    template_name = 'Normativa/crear.html'
    success_url = reverse_lazy('app:normativa_listar')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar una Normativa'
        context['entidad'] = 'Normativa'
        context['listar_url'] = reverse_lazy('app:normativa_listar')
        return context

class NormativaDeleteView(DeleteView):
    model = Normativa
    template_name = 'Normativa/eliminar.html'
    success_url = reverse_lazy('app:normativa_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar una Normativa'
        context['entidad'] = 'Normativas'
        context['listar_url'] = reverse_lazy('app:normativa_listar')
        return context