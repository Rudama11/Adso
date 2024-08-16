from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from app.models import Persona
from app.forms import PersonaForm
from app.choices import Roles, Tipo_Documento_Choices  # Asegúrate de importar tus choices aquí

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
        context['roles'] = Roles
        context['tipo_documento'] = Tipo_Documento_Choices
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        rol = self.request.GET.get('rol')
        nombres = self.request.GET.get('nombres')
        apellidos = self.request.GET.get('apellidos')
        tipo_documento = self.request.GET.get('tipo_documento')
        correo = self.request.GET.get('correo')
        telefono = self.request.GET.get('telefono')
        numero_documento = self.request.GET.get('numero_documento')
        usuario = self.request.GET.get('usuario')
        password = self.request.GET.get('password')

        if rol:
            queryset = queryset.filter(rol=rol)
        if nombres:
            queryset = queryset.filter(nombres__icontains=nombres)
        if apellidos:
            queryset = queryset.filter(apellidos__icontains=apellidos)
        if tipo_documento:
            queryset = queryset.filter(tipo_documento=tipo_documento)
        if correo:
            queryset = queryset.filter(correo__icontains=correo)
        if telefono:
            queryset = queryset.filter(telefono__icontains=telefono)
        if numero_documento:
            queryset = queryset.filter(numero_documento__icontains=numero_documento)
        if usuario:
            queryset = queryset.filter(usuario__icontains=usuario)
        if password:
            queryset = queryset.filter(password__icontains=password)

        return queryset

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