from django import forms
from goozs.models import Gooz

class RegisterForm(forms.Form):


    class Meta:
        model = Gooz
        fields = ('name', 'serial', 'photo')
