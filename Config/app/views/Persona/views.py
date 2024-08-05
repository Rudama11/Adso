
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from app.models import Persona
from app.forms import PersonaForm  

class PersonaListView(ListView):
    model = Persona
    template_name = 'Persona/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data = {'Nombre': 'Lorena'}
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Personas'
        context['entidad'] = 'Persona'
        context['crear_url'] = reverse_lazy('app:persona_crear')
        return context

class PersonaCreateView(CreateView):
    model = Persona
    form_class = PersonaForm  
    template_name = 'Persona/crear.html'
    success_url = reverse_lazy('app:persona_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Persona'
        context['entidad'] = 'Persona'
        context['listar_url'] = reverse_lazy('app:persona_listar')
        return context

class PersonaUpdateView(UpdateView):
    model = Persona
    form_class = PersonaForm 
    template_name = 'Persona/crear.html'
    success_url = reverse_lazy('app:persona_listar')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Persona'
        context['entidad'] = 'Persona'
        context['listar_url'] = reverse_lazy('app:persona_listar')
        return context

class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = 'Persona/eliminar.html'
    success_url = reverse_lazy('app:persona_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Persona'
        context['entidad'] = 'Persona'
        context['listar_url'] = reverse_lazy('app:persona_listar')
        return context