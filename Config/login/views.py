# from typing import Any
# from django.http import HttpRequest
# from django.http.response import HttpResponse as HttpResponse
# from django.shortcuts import redirect,render
# from django.views.generic import RedirectView
# from django.contrib.auth.views import LoginView
# from django.contrib.auth import login,logout 
# # Create your views here.

from django.shortcuts import render,redirect
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout

class LoginFormView(LoginView):
    template_name="login.html"
    
    def dispatch(self, request, **kwargs):
        if request.user.is_authenticated:
            return redirect("app:categoria_listar")
        return super().dispatch(request, **kwargs)
            
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ["titulo"] = "Iniciar Sesion"
        return context

class logoutredirect(RedirectView):
    pattern_name="login"
    
    def dispatch(self, request,*kwargs ):
        logout(request)
        return super().dispatch(request, *kwargs)
    
 