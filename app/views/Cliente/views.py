from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from app.models import Cliente
from app.forms import ClienteForm
from app.choices import Tipo_Documento_Choices, Tipo_Persona_Choices
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_POST
from app.mixins import LoginRequiredMixin

class ClienteListView(LoginRequiredMixin,ListView):
    model = Cliente
    template_name = 'Cliente/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Clientes'
        context['entidad'] = 'Cliente'
        context['crear_url'] = reverse_lazy('app:cliente_crear')
        context['tipo_documento'] = Tipo_Documento_Choices
        context['tipo_persona'] = Tipo_Persona_Choices
        # Agregar breadcrumbs
        context['breadcrumbs'] = [
            {'nombre': 'Modulo', 'url': '/dashboard'},
            {'nombre': 'Cliente', 'url': reverse_lazy('app:cliente_listar')},
        ]
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
    
    @require_POST
    @user_passes_test(lambda u: u.is_superuser or u.is_staff)
    def EliminarCliente(request, id_cliente):
        try:
            cliente = get_object_or_404(Cliente, pk=id_cliente)
            cliente.delete()
            return JsonResponse({'status': 'success', 'message': 'Cliente eliminado correctamente'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

class ClienteCreateView(LoginRequiredMixin,CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'Cliente/crear.html'
    success_url = reverse_lazy('app:cliente_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Cliente'
        context['entidad'] = 'Cliente'
        context['listar_url'] = reverse_lazy('app:cliente_listar')
        # Agregar breadcrumbs
        context['breadcrumbs'] = [
            {'nombre': 'Modulo', 'url': '/'},
            {'nombre': 'Cliente', 'url': reverse_lazy('app:cliente_listar')},
            {'nombre': 'Crear Cliente', 'url': reverse_lazy('app:cliente_crear')},
        ]
        
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

class ClienteUpdateView(LoginRequiredMixin,UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'Cliente/editarCli.html'
    success_url = reverse_lazy('app:cliente_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Cliente'
        context['entidad'] = 'Cliente'
        context['listar_url'] = reverse_lazy('app:cliente_listar')
        # Añadir breadcrumbs
        context['breadcrumbs'] = [
            {'nombre': 'Modulo', 'url': '/dashboard'},
            {'nombre': 'Cliente', 'url': reverse_lazy('app:cliente_listar')},
            {'nombre': 'Editar Cliente', 'url': reverse_lazy('app:cliente_editarCli', args=[self.object.pk])},
        ]

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