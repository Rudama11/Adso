from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.http import JsonResponse
from app.models import Cliente
from app.forms import ClienteForm
from app.choices import Tipo_Documento_Choices, Tipo_Persona_Choices
from django.shortcuts import redirect

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

        return queryset
    
    def EliminarCliente(request, id_cliente):
        cliente = Cliente.objects.get(pk=id_cliente)
        cliente.delete()
        return redirect('app:cliente_listar')

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'Cliente/crear.html'
    success_url = reverse_lazy('app:cliente_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Cliente'
        context['entidad'] = 'Cliente'
        context['listar_url'] = reverse_lazy('app:cliente_listar')
        return context

    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Cliente creado exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)

class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'Cliente/editarCli.html'
    success_url = reverse_lazy('app:cliente_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cliente'
        context['entidad'] = 'Cliente'
        context['listar_url'] = reverse_lazy('app:cliente_listar')
        return context

    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Cliente actualizado exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)