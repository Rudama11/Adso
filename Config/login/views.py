# from django.shortcuts import render,redirect
# from django.http.response import HttpResponse as HttpResponse
# from django.views.generic import RedirectView
# from django.contrib.auth.views import LoginView
# from django.contrib.auth import login, logout

# class LoginFormView(LoginView):
#     template_name="login.html"
    
#     def dispatch(self, request, **kwargs):
#         if request.user.is_authenticated:
#             return redirect("app:categoria_listar")
#         return super().dispatch(request, **kwargs)
            
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context ["titulo"] = "Iniciar Sesion"
#         return context

# class logoutredirect(RedirectView):
#     pattern_name="login"
    
#     def dispatch(self, request,*kwargs ):
#         logout(request)
#         return super().dispatch(request, *kwargs)
# login/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views.generic import RedirectView
from django.views.generic.edit import FormView
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import UserEmailForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.contrib.staticfiles import finders

class LoginFormView(LoginView):
    template_name = "login.html"
    
    def dispatch(self, request, **kwargs):
        if request.user.is_authenticated:
            return redirect("app:categoria_listar")
        return super().dispatch(request, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Iniciar Sesión"
        return context

class logoutredirect(RedirectView):
    pattern_name = "login"
    
    def dispatch(self, request, *kwargs):
        logout(request)
        return super().dispatch(request, *kwargs)

class UserEmailValidationView(FormView):
    template_name = 'validate_email.html'
    form_class = UserEmailForm
    success_url = reverse_lazy('success_page')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        messages.success(self.request, f'El correo {email} existe en el sistema.')
        return super().form_valid(form)
 
def send_password_reset_email(user_email, reset_url, user):
    subject = 'Restablece tu contraseña'
    html_content = render_to_string('password_reset_email.html', {'reset_url': reset_url, 'user': user})
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.EMAIL_HOST_USER,  # Usa el correo del settings
        to=[user_email]
    )

    # Adjuntar la imagen del logo
    logo_path = finders.find('img/logoConaldex.jfif')
    if logo_path:
        with open(logo_path, 'rb') as logo_file:
            email.attach(logo_file.name, logo_file.read(), 'image/jpeg')
    
    email.attach_alternative(html_content, 'text/html')
    email.send()