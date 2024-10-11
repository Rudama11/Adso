from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from app.models import Normativa
from app.forms import NormativaForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_POST
from app.mixins import LoginRequiredMixin

class NormativaListView(LoginRequiredMixin,ListView):
    model = Normativa
    template_name = 'Normativa/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Normativas'
        context['entidad'] = 'Normativas'
        context['crear_url'] = reverse_lazy('app:normativa_crear')
        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        id = self.request.GET.get('id')
        decreto = self.request.GET.get('decreto')
        descripcion = self.request.GET.get('descripcion')
        producto = self.request.GET.get('producto')

        if id:
            queryset = queryset.filter(id=id)
        if decreto:
            queryset = queryset.filter(decreto__icontains=decreto)
        if descripcion:
            queryset = queryset.filter(descripcion__icontains=descripcion)
        if producto:
            queryset = queryset.filter(producto__icontains=producto)
        
        return queryset

    @require_POST
    @user_passes_test(lambda u: u.is_superuser or u.is_staff)
    def EliminarNormativa(request, id_norma):
        try:
            norma = get_object_or_404(Normativa, pk=id_norma)
            norma.delete()
            return JsonResponse({'status': 'success', 'message': 'Normativa eliminada correctamente'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

class NormativaCreateView(LoginRequiredMixin,CreateView):
    model = Normativa
    form_class = NormativaForm
    template_name = 'Normativa/crear.html'
    success_url = reverse_lazy('app:normativa_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Normativa'
        context['entidad'] = 'Normativas'
        context['listar_url'] = reverse_lazy('app:normativa_listar')
        return context

    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Normativa creada exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)

class NormativaUpdateView(LoginRequiredMixin,UpdateView):
    model = Normativa
    form_class = NormativaForm
    template_name = 'Normativa/editarN.html'
    success_url = reverse_lazy('app:normativa_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Editar Normativa'
        context['entidad'] = 'Normativa'
        context['listar_url'] = reverse_lazy('app:normativa_listar')
        return context
    
    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Normativa actualizada exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)