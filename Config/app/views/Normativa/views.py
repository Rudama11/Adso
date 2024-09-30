from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.http import JsonResponse
from django.urls import reverse_lazy
from app.models import Normativa
from app.forms import NormativaForm
from django.shortcuts import redirect

class NormativaListView(ListView):
    model = Normativa
    template_name = 'Normativa/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data = {'Nombre': 'Lorena'}
        return JsonResponse(data)
    
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
    
    def EliminarNormativa(request, id_norma):
        norma = Normativa.objects.get(pk=id_norma)
        norma.delete()
        return redirect('app:normativa_listar')

class NormativaCreateView(CreateView):
    model = Normativa
    form_class = NormativaForm
    template_name = 'Normativa/crear.html'
    success_url = reverse_lazy('app:normativa_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Normativa'
        context['entidad'] = 'Normativa'
        context['listar_url'] = reverse_lazy('app:normativa_listar')
        return context
    
    def form_valid(self, form):
        # Verificar si el campo de descripción está vacío
        if not form.cleaned_data.get('descripcion'):
            return JsonResponse({
                'status': 'error',
                'message': 'El campo de descripción es obligatorio.'
            }, status=400)

        # Guardar la normativa
        self.object = form.save()

        return JsonResponse({
            'status': 'success',
            'message': 'Normativa creada correctamente'
        })

    def form_invalid(self, form):
        # Preparar los errores para respuesta JSON
        errors = form.errors.as_json()
        return JsonResponse({
            'status': 'error',
            'message': 'Error al crear la normativa. Verifica los campos.',
            'errors': errors
        }, status=400)

class NormativaUpdateView(UpdateView):
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
        # Verificar si la descripción está vacía
        if not form.cleaned_data.get('descripcion'):
            return JsonResponse({
                'status': 'error',
                'message': 'El campo de descripción es obligatorio.'
            }, status=400)

        # Guardar la normativa
        self.object = form.save()
        return JsonResponse({
            'status': 'success',
            'message': 'Normativa actualizada correctamente'
        })
    
    def form_invalid(self, form):
        # Enviar los errores de validación en formato JSON
        errors = form.errors.as_json()
        return JsonResponse({
            'status': 'error',
            'errors': errors
        }, status=400)