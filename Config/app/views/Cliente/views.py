from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from typing import Any
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.http.response import HttpResponse as HttpResponse
from app.models import Cliente
from app.forms import ClienteForm

@login_required
def lista_cliente(request):
    context = {
        'titulo': 'Listado de Clientes',
        'clientes': Cliente.objects.all(),
        'crear_url': reverse_lazy('app:cliente_crear')  # Asegúrate de tener esta línea
    }
    return render(request, 'Cliente/listarC.html', context)

class ClienteListView(ListView):
    model = Cliente
    template_name = 'Cliente/listarC.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data = {'Nombre': 'Lorena'}
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Clientes'
        context['entidad'] = 'Cliente'
        context['crear_url'] = reverse_lazy('app:cliente_crear')
        return context

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'Cliente/crearC.html'
    success_url = reverse_lazy('app:cliente_listarC')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Cliente'
        context['entidad'] = 'Cliente'
        context['listar_url'] = reverse_lazy('app:cliente_listarC')
        return context

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'Cliente/crearC.html'
    success_url = reverse_lazy('app:cliente_listarC')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Cliente'
        context['entidad'] = 'Cliente'
        context['listar_url'] = reverse_lazy('app:cliente_listarC')
        return context

class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'Cliente/eliminarC.html'
    success_url = reverse_lazy('app:cliente_listarC')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Cliente'
        context['entidad'] = 'Cliente'
        context['listar_url'] = reverse_lazy('app:cliente_listarC')
        return context