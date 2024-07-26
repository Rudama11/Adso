from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
# Create your views here.

class IndexView(TemplateView):
    template_name ='index.html'
    # views.py en la aplicación 'inicio'

@csrf_protect
def enviar_correo(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')

            if not all([name, email, subject, message]):
                raise ValueError("Todos los campos son obligatorios.")

            # Mejorar el mensaje
            full_message = (
                f"Nuevo mensaje recibido:\n\n"
                f"Nombre: {name}\n"
                f"Email: {email}\n"
                f"Asunto: {subject}\n\n"
                f"Mensaje:\n{message}\n\n"
                f"Este mensaje ha sido enviado desde el formulario de contacto de la pagina de Conaldex."
            )

            # Enviar el correo
            send_mail(
                subject,  # Asunto
                full_message,  # Mensaje mejorado
                settings.DEFAULT_FROM_EMAIL,  # De
                ["boyacaconaldex@gmail.com"],  # Para
                fail_silently=False,
            )
            
            return JsonResponse({'message': 'La información se envió correctamente!!!', 'error': 'false'}, status=200)
        
        except ValueError as ve:
            return JsonResponse({'message': str(ve), 'error': 'true'}, status=400)
        except Exception as e:
            return JsonResponse({'message': 'Error al enviar el correo: ' + str(e), 'error': 'true'}, status=500)
    
    return JsonResponse({'message': 'No hemos podido completar la solicitud. {enviar_correo} no found', 'error': 'true'}, status=405)
