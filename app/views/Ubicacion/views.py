from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from app.models import Ubicacion,Departamentos,Municipios
from app.forms import UbicacionForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_POST
from app.mixins import LoginRequiredMixin

class UbicacionListView(LoginRequiredMixin,ListView):
    model = Ubicacion
    template_name = 'Ubicacion/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Ubicaciones'
        context['entidad'] = 'Ubicacion'
        context['crear_url'] = reverse_lazy('app:ubicacion_crear')
        context['departamentos'] = Departamentos.objects.all()
        context['municipios'] = Municipios.objects.all()
       # Agregar breadcrumbs
        context['breadcrumbs'] = [
            {'nombre': 'Modulos', 'url': '/dashboard'},
            {'nombre': 'Ubicación', 'url': reverse_lazy('app:ubicacion_listar')},
        ]
        return context
    

    def get_queryset(self):
        queryset = super().get_queryset()

        departamento_id = self.request.GET.get('departamento')
        municipio_id = self.request.GET.get('municipio')

        if departamento_id:
            queryset = queryset.filter(departamento_id=departamento_id)
        if municipio_id:
            queryset = queryset.filter(municipio_id=municipio_id)

        return queryset
        
    @require_POST
    @user_passes_test(lambda u: u.is_superuser or u.is_staff)
    def EliminarUbicacion(request, id_ubica):
        try:
            ubica = get_object_or_404(Ubicacion, pk=id_ubica)
            ubica.delete()
            return JsonResponse({'status': 'success', 'message': 'Ubicacion eliminada correctamente'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

class UbicacionCreateView(LoginRequiredMixin,CreateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'Ubicacion/crear.html'
    success_url = reverse_lazy('app:ubicacion_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Crear Ubicación'  # Corregir título
        context['entidad'] = 'Ubicación'  # Cambiar entidad a 'Ubicación'
        context['listar_url'] = reverse_lazy('app:ubicacion_listar')  # Cambiar la URL a la lista de ubicaciones
           # Agregar breadcrumbs
        context['breadcrumbs'] = [
            {'nombre': 'Modulos', 'url': '/dashboard'},
            {'nombre': 'Ubicación', 'url': reverse_lazy('app:ubicacion_listar')},
            {'nombre': 'Crear Ubicación', 'url': reverse_lazy('app:ubicacion_crear')},
        ]
        
        return context
    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Ubicación creada exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)

def municipios_por_departamento(request):
    departamento_id = request.GET.get('departamento_id')
    if departamento_id:
        municipios = Municipios.objects.filter(departamento_id=departamento_id).values('id', 'nombre')
    else:
        municipios = []
    return JsonResponse({'municipios': list(municipios)})