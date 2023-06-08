from django import forms
from .models import *


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__"

        
