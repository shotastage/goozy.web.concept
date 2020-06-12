from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, FormView, ListView
from goozs.models import Gooz

# Create your views here.


class GoozsIndexView(ListView):
    template_name = "index.html"
    paginate_by = 20

    model = Gooz


class GoozsCreateView(CreateView):
    template_name = "register.html"

    model = Gooz
    fields = ['name', 'serial', 'photo']
    success_url = "/"



    def get_form(self):
        form = super(GoozsCreateView, self).get_form()
        form.fields['name'].label = '品名'
        form.fields['serial'].label = 'シリアル'

        return form
