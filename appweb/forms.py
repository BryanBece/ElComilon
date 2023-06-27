from django import forms
from .models import *


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__"

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"


from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            User = get_user_model()
            user = User.objects.filter(username=username).first()
            if user is None or not user.check_password(password):
                raise forms.ValidationError('Nombre de usuario o contraseña incorrectos.')
        return cleaned_data
        
