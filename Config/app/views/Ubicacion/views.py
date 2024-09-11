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
    template_name = 'Ubicacion/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Ubicaciones'
        context['entidad'] = 'Ubicacion'
        context['crear_url'] = reverse_lazy('app:ubicacion_crear')
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
            queryset = queryset.filter(municipio_id=municipio_id)

        return queryset

class UbicacionCreateView(CreateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'Ubicacion/crear.html'
    success_url = reverse_lazy('app:ubicacion_listar')

    def form_invalid(self, form):
        response = super().form_invalid(form)
        if form.non_field_errors():
            print("Error no relacionado con los campos: ", form.non_field_errors())
        return response

class UbicacionUpdateView(UpdateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'Ubicacion/editarUbi.html'
    success_url = reverse_lazy('app:ubicacion_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Ubicación'
        context['entidad'] = 'Ubicacion'
        context['listar_url'] = reverse_lazy('app:ubicacion_listar')
        return context

class UbicacionDeleteView(DeleteView):
    model = Ubicacion
    template_name = 'Ubicacion/eliminar.html'
    success_url = reverse_lazy('app:ubicacion_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Ubicación'
        context['entidad'] = 'Ubicacion'
        context['listar_url'] = reverse_lazy('app:ubicacion_listar')
        return context

def municipios_por_departamento(request):
    departamento_id = request.GET.get('departamento_id')
    if departamento_id:
        municipios = Municipios.objects.filter(departamento_id=departamento_id).values('id', 'nombre')
    else:
        municipios = []
    return JsonResponse({'municipios': list(municipios)})