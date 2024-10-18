from django.urls import reverse_lazy
from django.views.generic import ListView
from app.models import Stock
from app.forms import StockFilterForm
from app.mixins import LoginRequiredMixin

class StockListView(LoginRequiredMixin,ListView):
    model = Stock
    template_name = 'Stock/listar.html'
    context_object_name = 'stocks'

    def get_queryset(self):
        queryset = super().get_queryset()
        form = StockFilterForm(self.request.GET or None)
        if form.is_valid():
            nombre_pro = form.cleaned_data.get('nombre_pro')
            cantidad_min = form.cleaned_data.get('cantidad_min')
            cantidad_max = form.cleaned_data.get('cantidad_max')
            precio_min = form.cleaned_data.get('precio_min')
            precio_max = form.cleaned_data.get('precio_max')

            if nombre_pro:
                queryset = queryset.filter(nombre_pro=nombre_pro)
            if cantidad_min is not None:
                queryset = queryset.filter(cantidad__gte=cantidad_min)
            if cantidad_max is not None:
                queryset = queryset.filter(cantidad__lte=cantidad_max)
            if precio_min is not None:
                queryset = queryset.filter(precio__gte=precio_min)
            if precio_max is not None:
                queryset = queryset.filter(precio__lte=precio_max)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Stocks'
        context['entidad'] = 'Stocks'
        context['form'] = StockFilterForm(self.request.GET or None)  # Agregamos el formulario de filtros
        context['breadcrumbs'] = [
            {'nombre': 'Modulos', 'url': '/dashboard'},
            {'nombre': 'Modulo Stock', 'url': reverse_lazy('app:listar_stock')},
        ]
        return context