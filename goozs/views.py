from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView
from goozs.models import Gooz
# Create your views here.


class GoozsIndexView(TemplateView):
    template_name = "index.html"


class GoozsCreateView(CreateView):
    template_name = "register.html"

    model = Gooz
    fields = ['name', 'serial', 'photo', 'registered_by']
    success_url = "/"
