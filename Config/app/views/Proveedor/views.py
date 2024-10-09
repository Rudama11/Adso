from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView
from app.models import Proveedor
from app.forms import ProveedorForm
from app.choices import Tipo_Documento_Choices, Tipo_Persona_Choices
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_POST
class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'Proveedor/listar.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Proveedores'
        context['entidad'] = 'Proveedores'
        context['crear_url'] = reverse_lazy('app:proveedor_crear')
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

    @require_POST
    @user_passes_test(lambda u: u.is_superuser or u.is_staff)
    def EliminarProveedor(request, id_prove):
        try:
            prove = get_object_or_404(Proveedor, pk=id_prove)
            prove.delete()
            return JsonResponse({'status': 'success', 'message': 'Proveedor eliminado correctamente'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    
class ProveedorCreateView(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'Proveedor/crear.html'
    success_url = reverse_lazy('app:proveedor_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Proveedor'
        context['entidad'] = 'Proveedor'
        context['listar_url'] = reverse_lazy('app:proveedor_listar')
        return context

    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Proveedor creado exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'Proveedor/editarProv.html'
    success_url = reverse_lazy('app:proveedor_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Proveedor'
        context['entidad'] = 'Proveedor'
        context['listar_url'] = reverse_lazy('app:proveedor_listar')
        return context

    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Proveedor actualizado exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)