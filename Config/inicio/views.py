from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
from django.http import JsonResponse

# Create your views here.

class IndexView(TemplateView):
    template_name ='index.html'
    # views.py en la aplicación 'inicio'

def enviar_correo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        message += " Este es el nombre: "+ name + " email: " + email
        

        # Enviar el correo
        send_mail(
            subject,  # Asunto
            message,  # Mensaje
            settings.DEFAULT_FROM_EMAIL,  # De
            ["boyacaconaldex@gmail.com"],  # Para
            fail_silently=False,
            
        )
        #return render(request, 'index.html', {'message': 'Your message has been sent. Thank you!'})
        #return HttpResponse(status=200)
        return JsonResponse({'message': 'Your message has been sent. Thank you!'}, status=200)
        #return JsonResponse({'status': 'OK'})
    
    #return HttpResponse(status=405)
    return JsonResponse({'error': 'Method Not Allowed enviar_correo no found'}, status=405)
