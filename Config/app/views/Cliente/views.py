from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from app.models import Cliente
from app.forms import ClienteForm
from django.contrib import messages
from app.choices import Tipo_Documento_Choices, Tipo_Persona_Choices  # Asegúrate de importar tus choices aquí

class ClienteListView(ListView):
    model = Cliente
    template_name = 'Cliente/listar.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Clientes'
        context['entidad'] = 'Cliente'
        context['crear_url'] = reverse_lazy('app:cliente_crear')
        context['tipo_documento'] = Tipo_Documento_Choices
        context['tipo_persona'] = Tipo_Persona_Choices
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        # Obtener los parámetros GET
        tipo_persona = self.request.GET.get('tipo_persona')
        nombres = self.request.GET.get('nombres')
        tipo_documento = self.request.GET.get('tipo_documento')
        correo = self.request.GET.get('correo')
        telefono = self.request.GET.get('telefono')
        numero_documento = self.request.GET.get('numero_documento')
        usuario = self.request.GET.get('usuario')
        password = self.request.GET.get('password')

        # Aplicar filtros si los parámetros existen
        if tipo_persona:
            queryset = queryset.filter(tipo_persona=tipo_persona)
        if nombres:
            queryset = queryset.filter(nombres__icontains=nombres)
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

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'Cliente/crear.html'
    success_url = reverse_lazy('app:cliente_listar')

    def form_valid(self, form):
        messages.success(self.request, 'Cliente creado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'No se pudo crear el cliente. Verifica los errores.')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Cliente'
        context['entidad'] = 'Cliente'
        context['listar_url'] = reverse_lazy('app:cliente_listar')
        return context

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'Cliente/editarCli.html'
    success_url = reverse_lazy('app:cliente_listar')

    def form_valid(self, form):
        messages.success(self.request, 'Cliente actualizado exitosamente.')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'No se pudo actualizar el cliente. Verifica los errores.')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Cliente'
        context['entidad'] = 'Cliente'
        context['listar_url'] = reverse_lazy('app:cliente_listar')
        return context
    
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'Cliente/eliminar.html'
    success_url = reverse_lazy('app:cliente_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Eliminar Cliente'
        context['entidad'] = 'Cliente'
        context['listar_url'] = reverse_lazy('app:cliente_listar')
        return context