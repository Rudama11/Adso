from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from app.models import Tipo
from app.forms import TipoForm

class TipoListView(ListView):
    model = Tipo
    template_name = 'Tipo/listarT.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data = {'Nombre': 'Lorena'}
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Tipos'
        context['entidad'] = 'Tipos'
        context['crear_url'] = reverse_lazy('app:tipo_crear')
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        id = self.request.GET.get('id')
        nombre = self.request.GET.get('nombre')
        descripcion = self.request.GET.get('descripcion')

        if id:
            queryset = queryset.filter(id=id)
        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        if descripcion:
            queryset = queryset.filter(descripcion__icontains=descripcion)
        
        return queryset

class TipoCreateView(CreateView):
    model = Tipo
    form_class = TipoForm
    template_name = 'Tipo/crearT.html'
    success_url = reverse_lazy('app:tipo_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Tipos'
        context['entidad'] = 'Tipo'
        context['listar_url'] = reverse_lazy('app:tipo_listar')
        return context

class TipoUpdateView(UpdateView):
    model = Tipo
    form_class = TipoForm
    template_name = 'Tipo/crearT.html'
    success_url = reverse_lazy('app:tipo_listar')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Tipo'
        context['entidad'] = 'Tipo'
        context['listar_url'] = reverse_lazy('app:tipo_listar')
        return context

class TipoDeleteView(DeleteView):
    model = Tipo
    template_name = 'Tipo/eliminarT.html'
    success_url = reverse_lazy('app:tipo_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Tipo'
        context['entidad'] = 'Tipo'
        context['listar_url'] = reverse_lazy('app:tipo_listar')
        return context