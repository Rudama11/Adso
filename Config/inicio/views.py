from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail, EmailMessage
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_protect

class IndexView(TemplateView):
    template_name = 'index.html'

@csrf_protect
def enviar_correo(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            image = request.FILES.get('image')

            if not all([name, email, subject, message]):
                raise ValueError("Todos los campos son obligatorios.")

            # Mejorar el mensaje
            full_message = (
                f"Nuevo mensaje recibido:\n\n"
                f"Nombre: {name}\n"
                f"Email: {email}\n"
                f"Asunto: {subject}\n\n"
                f"Mensaje:\n{message}\n\n"
                f"Este mensaje ha sido enviado desde el formulario de contacto de la página de Conaldex."
            )

            # Enviar el correo
            email_message = EmailMessage(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                ["boyacaconaldex@gmail.com"],
            )

            if image:
                email_message.attach(image.name, image.read(), image.content_type)

            email_message.send(fail_silently=False)
            
            return JsonResponse({'message': 'La información se envió correctamente!!!', 'error': 'false'}, status=200)
        
        except ValueError as ve:
            return JsonResponse({'message': str(ve), 'error': 'true'}, status=400)
        except Exception as e:
            return JsonResponse({'message': 'Error al enviar el correo: ' + str(e), 'error': 'true'}, status=500)
    
    return JsonResponse({'message': 'No hemos podido completar la solicitud. {enviar_correo} no found', 'error': 'true'}, status=405)
