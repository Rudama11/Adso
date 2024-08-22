from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from typing import Any
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.http.response import HttpResponse as HttpResponse
from app.models import Ubicacion,Departamentos,Municipios
from app.forms import UbicacionForm

class UbicacionListView(ListView):
    model = Ubicacion
    template_name = 'Ubicacion/listarU.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Ubicaciones'
        context['entidad'] = 'Ubicacion'
        context['crear_url'] = reverse_lazy('app:ubicacion_crear')
        
        # Obtener todos los departamentos y municipios
        context['departamentos'] = Departamentos.objects.all()
        context['municipios'] = Municipios.objects.all()
        
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        departamento_id = self.request.GET.get('departamento')
        municipio_id = self.request.GET.get('municipio')

        if departamento_id:
            queryset = queryset.filter(departamento_id=departamento_id)
        if municipio_id:
            queryset = queryset.filter(ciudad_id=municipio_id)

        return queryset

class UbicacionCreateView(CreateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'Ubicacion/crearU.html'
    success_url = reverse_lazy('app:ubicacion_listarU')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Ubicacion'
        context['entidad'] = 'Ubicacion'
        context['listar_url'] = reverse_lazy('app:ubicacion_listarU')
        return context

    def get(self, request, *args, **kwargs):
        # Verifica si la solicitud es AJAX
        if 'X-Requested-With' in request.headers and request.headers['X-Requested-With'] == 'XMLHttpRequest':
            # Lógica para solicitudes AJAX (si es necesario)
            data = {'message': 'Esta es una respuesta AJAX'}
            return JsonResponse(data)
        else:
            return super().get(request, *args, **kwargs)

class UbicacionUpdateView(UpdateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'Ubicacion/crearU.html'
    success_url = reverse_lazy('app:ubicacion_listarU')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Ubicacion'
        context['entidad'] = 'Ubicacion'
        context['listar_url'] = reverse_lazy('app:ubicacion_listarU')
        return context

class UbicacionDeleteView(DeleteView):
    model = Ubicacion
    template_name = 'Ubicacion/eliminarU.html'
    success_url = reverse_lazy('app:ubicacion_listarU')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Ubicacion'
        context['entidad'] = 'Ubicacion'
        context['listar_url'] = reverse_lazy('app:ubicacion_listarU')
        return context

def municipios_por_departamento(request):
    codigo_departamento = request.GET.get('departamento_id')
    municipios = Municipios.objects.filter(cod_departamento_id=codigo_departamento).values('id', 'nombre')
    return JsonResponse({'municipios': list(municipios)})