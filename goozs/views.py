from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from goozs.models import Gooz

# Create your views here.


class GoozsIndexView(LoginRequiredMixin, ListView):
    login_url = '/account/login/'
    redirect_field_name = 'redirect_to'
    template_name = "index.html"
    paginate_by = 10

    def get_queryset(self):
        print(self.kwargs.get('username'))
        return Gooz.objects.filter(registered_by=self.request.user)



class GoozsCreateView(LoginRequiredMixin, CreateView):
    template_name = "register.html"
    login_url = '/account/login/'
    redirect_field_name = 'redirect_to'
    model = Gooz
    fields = ['name', 'serial', 'photo', 'registered_by']
    success_url = "/"



    def get_form(self):
        form = super(GoozsCreateView, self).get_form()
        form.fields['name'].label = '品名'
        form.fields['serial'].label = 'シリアル'

        return form
