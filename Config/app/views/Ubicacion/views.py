from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from typing import Any
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.http.response import HttpResponse as HttpResponse
from app.models import Ubicacion
from app.forms import UbicacionForm
from app.choices import Departamentos,Ciudades

@login_required
def lista_ubicacion(request):
    context = {
        'titulo': 'Listado de Ubicaciones',
        'ubicaciones': Ubicacion.objects.all(),
        'crear_url': reverse_lazy('app:ubicacion_crear')  # Asegúrate de tener esta línea
    }
    return render(request, 'Ubicacion/listarU.html', context)
class UbicacionListView(ListView):
    model = Ubicacion
    template_name = 'Ubicacion/listarU.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data = {'Nombre': 'Lorena'}
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Ubicaciones'
        context['entidad'] = 'Ubicacion'
        context['crear_url'] = reverse_lazy('app:ubicacion_crear')
        
         # Obtener las opciones de choices
        context['departamentos'] = Departamentos  # Asegúrate de que Departamentos sea un iterable de opciones
        context['ciudades'] = Ciudades  # Asegúrate de que Ciudades sea un iterable de opciones
        
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Obtener los parámetros GET
        departamento = self.request.GET.get('departamento')
        ciudad = self.request.GET.get('ciudad')

        # Aplicar filtros si los parámetros existen
        if departamento:
            queryset = queryset.filter(departamento=departamento)
        if ciudad:
            queryset = queryset.filter(ciudad=ciudad)

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
