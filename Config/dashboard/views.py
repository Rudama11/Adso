from django.shortcuts import render
from django.views.generic import TemplateView

class dashView(TemplateView):
    template_name = 'dashboard.html'
