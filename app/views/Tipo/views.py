from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from app.models import Tipo
from app.forms import TipoForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_POST
from app.mixins import LoginRequiredMixin

class TipoListView(LoginRequiredMixin,ListView):
    model = Tipo 
    template_name = 'Tipo/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado Tipos de producto'
        context['entidad'] = 'Tipos de producto'
        context['crear_url'] = reverse_lazy('app:tipo_crear')
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        nombre = self.request.GET.get('nombre')
        descripcion = self.request.GET.get('descripcion')

        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        if descripcion:
            queryset = queryset.filter(descripcion__icontains=descripcion)
        
        return queryset
    
    @require_POST  # Asegura que solo se pueda eliminar con POST
    @user_passes_test(lambda u: u.is_superuser or u.is_staff)
    def EliminarTipo(request, id_tipo):
        try:
            tipo = get_object_or_404(Tipo, pk=id_tipo)
            tipo.delete()
            return JsonResponse({'status': 'success', 'message': 'Tipo producto eliminado correctamente'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

class TipoCreateView(LoginRequiredMixin,CreateView):
    model = Tipo
    form_class = TipoForm
    template_name = 'Tipo/crear.html'
    success_url = reverse_lazy('app:tipo_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Tipos de producto'
        context['entidad'] = 'Tipo'
        context['listar_url'] = reverse_lazy('app:tipo_listar')
        return context
    
    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Tipo producto creado exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)

class TipoUpdateView(LoginRequiredMixin,UpdateView):
    model = Tipo
    form_class = TipoForm
    template_name = 'Tipo/editarTP.html'
    success_url = reverse_lazy('app:tipo_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Tipo de Producto'
        context['entidad'] = 'Tipo'
        context['listar_url'] = reverse_lazy('app:tipo_listar')
        return context
    
    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Tipo producto actualizado exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)