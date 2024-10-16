from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.http import JsonResponse
from django.db import transaction
import json  
from app.forms import DetalleVentaForm
from app.models import DetalleVenta, Stock, Venta
from app.mixins import LoginRequiredMixin

class DetalleVentaListView(LoginRequiredMixin,ListView):
    model = DetalleVenta
    template_name = 'Dventas/listar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Listado de Detalles de Ventas'
        context['entidad'] = 'Detalle de Venta'
        context['crear_url'] = reverse_lazy('app:detalleventa_crear')
         # Agregar breadcrumbs
        context['breadcrumbs'] = [
            {'nombre': 'Modulos', 'url': '/dashboard'},
            {'nombre': 'Detalle Venta', 'url': reverse_lazy('app:detalleventa_listar')},
        ]
        return context


class VentaDetalleCreateView(LoginRequiredMixin,CreateView):
    model = DetalleVenta
    template_name = 'Ventas/VentaD.html'
    fields = ['producto', 'cantidad', 'precio', 'iva', 'total']  # Campos que se usarán en el formulario

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        venta = get_object_or_404(Venta, id=self.kwargs['venta_id'])  # Obtener la venta actual
        context['venta'] = venta
        context['detalles_venta_url'] = reverse('app:detalle_venta', kwargs={'venta_id': venta.id})
        context['detalles_venta'] = DetalleVenta.objects.filter(venta=venta)
        context['titulo'] = 'Detalles de Venta'
        context['listar_url'] = reverse('app:venta_listar')
        context['productos'] = Stock.objects.all()  # Obtener todos los productos
             # Agregar breadcrumbs
        context['breadcrumbs'] = [
            {'nombre': 'Modulos', 'url': '/dashboard'},
            {'nombre': 'Detalle Venta', 'url': reverse_lazy('app:detalleventa_listar')},
            
        ]
        
        return context

    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Categoria creada exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)

    def post(self, request, *args, **kwargs):
        # Asegurarse de que es una solicitud AJAX
        if request.headers.get('x-requested-with') != 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': 'Método no permitido'}, status=405)

        try:
            data = json.loads(request.body)

            # Verificar campos obligatorios
            required_keys = ['producto', 'cantidad', 'precio', 'iva', 'id_venta']
            if any(key not in data for key in required_keys):
                return JsonResponse({'success': False, 'error': 'Faltan campos requeridos.'}, status=400)

            # Obtener venta y producto, y validar cantidad solicitada
            venta = get_object_or_404(Venta, id=data['id_venta'])
            producto = get_object_or_404(Stock, id=data['producto'])

            cantidad = int(data['cantidad'])
            if cantidad <= 0:
                return JsonResponse({'success': False, 'error': 'La cantidad debe ser mayor que cero.'}, status=400)

            # Verificar stock disponible
            if producto.cantidad < cantidad:
                return JsonResponse({
                    'success': False,
                    'error': f"No hay suficiente stock para {producto.nombre_pro.nombre}. Stock actual: {producto.cantidad}, solicitado: {cantidad}"
                }, status=400)

            with transaction.atomic():
                # Crear el detalle de venta
                detalle_venta = DetalleVenta.objects.create(
                    producto=producto,
                    cantidad=cantidad,
                    precio=data['precio'],
                    iva=data['iva'],
                    total=data['precio'] * cantidad * (1 + (data['iva'] / 100)),
                    venta=venta,
                    num_factura=data.get('num_factura', "Factura Generada")
                )

                # Actualizar el stock del producto
                producto.cantidad -= cantidad
                producto.save()

            # Enviar respuesta exitosa
            return JsonResponse({'success': True, 'detalle_venta': detalle_venta.id, 'message': 'Detalle de venta agregado correctamente.'})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Error en los datos enviados.'}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)


class DetalleVentaUpdateView(LoginRequiredMixin,UpdateView):
    model = DetalleVenta
    form_class = DetalleVentaForm
    template_name = 'Dventas/editar.html'
    success_url = reverse_lazy('app:detalleventa_listar')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Actualizar Detalle de Venta'
        context['entidad'] = 'Detalle de Venta'
        context['listar_url'] = reverse_lazy('app:detalleventa_listar')
        # Añadir breadcrumbs
        context['breadcrumbs'] = [
            {'nombre': 'Modulos', 'url': '/dashboard'},
            {'nombre': 'Detalle Venta', 'url': reverse_lazy('app:detalleventa_listar')},
            {'nombre': 'Detalle Venta Editar', 'url': reverse_lazy('app:detalleventa_editar', args=[self.object.pk])},
        ]

        return context
    
    def form_valid(self, form):
        form.save()
        return JsonResponse({
            'success': True,
            'message': 'Categoria actualizada exitosamente',
        })

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
        return super().form_invalid(form)