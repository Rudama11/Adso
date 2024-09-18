from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from app.models import Categoria
from app.forms import CategoriaForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator

class CategoriaListView(ListView):
    model = Categoria
    template_name = 'Categoria/listar.html'
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Categorías'
        context['entidad'] = 'Categoría'
        context['crear_url'] = reverse_lazy('app:categoria_crear')
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


    @user_passes_test(lambda u: u.is_superuser or u.is_staff)
    def eliminar_categoria(request, id_categ):
        categ = get_object_or_404(Categoria, pk=id_categ)
        categ.delete()
        return redirect('app:categoria_listar')

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'Categoria/crear.html'
    success_url = reverse_lazy('app:categoria_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Categoría'
        context['entidad'] = 'Categoría'
        context['listar_url'] = reverse_lazy('app:categoria_listar')
        return context

    def form_valid(self, form):
        # Verificar si la descripción está vacía
        if not form.cleaned_data.get('descripcion'):
            return JsonResponse({
                'status': 'error',
                'message': 'El campo de descripción es obligatorio.'
            }, status=400)

        # Guardar la categoría explícitamente
        form.save()
        return JsonResponse({
            'status': 'success',
            'message': 'Categoría creada correctamente'
        })

    def form_invalid(self, form):
        # Si el formulario es inválido, enviamos los errores
        errors = form.errors.as_json()
        return JsonResponse({
            'status': 'error',
            'message': 'Ya existe una categoría con ese nombre o el formulario es inválido',
            'errors': errors
        }, status=400)


class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'Categoria/editarC.html'
    success_url = reverse_lazy('app:categoria_listar')

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True})
        return response

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors})
        return super().form_invalid(form)