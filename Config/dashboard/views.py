from django.shortcuts import render
from django.views.generic import TemplateView
from app.mixins import LoginRequiredMixin

class dashView(LoginRequiredMixin,TemplateView):
    template_name = 'dashboard.html'
