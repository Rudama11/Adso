from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class indexView(TemplateView):
    template_name ='index.html'