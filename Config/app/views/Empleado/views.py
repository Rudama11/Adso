
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from app.models import Empleado
from app.forms import EmpleadoForm  

class EmpleadoListView(ListView):
    model = Empleado
    template_name = 'Empleado/listarE.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data = {'Nombre': 'Lorena'}
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Empleado'
        context['entidad'] = 'Empleado'
        context['crear_url'] = reverse_lazy('app:empleado_crear')
        return context

class EmpleadoCreateView(CreateView):
    model = Empleado
    form_class = EmpleadoForm  
    template_name = 'Empleado/crearE.html'
    success_url = reverse_lazy('app:empleado_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Empleado'
        context['entidad'] = 'Empleado'
        context['listar_url'] = reverse_lazy('app:empleado_listar')
        return context

class EmpleadoUpdateView(UpdateView):
    model = Empleado
    form_class = EmpleadoForm 
    template_name = 'Empleado/crearV.html'
    success_url = reverse_lazy('app:empleado_listar')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Empleado'
        context['entidad'] = 'Empleado'
        context['listar_url'] = reverse_lazy('app:empleado_listar')
        return context

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = 'Empleado/eliminarV.html'
    success_url = reverse_lazy('app:empleado_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Empleado'
        context['entidad'] = 'Empleado'
        context['listar_url'] = reverse_lazy('app:empleado_listar')
        return context