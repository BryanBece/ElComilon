from django import forms
from .models import *


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__"

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "nombre", "descripcion", "precio", "imagen", "tipo_plato", "disponible", "origen"

class usuarioEmpresaForm(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = usuarioEmpresa
        fields = "nombre", "apellido", "correo", "contrasena", "saldo"

class pedidoForm(forms.ModelForm):

    class Meta:
        model = Pedido
        fields = ["nombre", "apellido", "telefono", "direccion", "programar_diariamente", "fecha_entrega", "hora_entrega"]
        widgets = {
            "fecha_entrega": forms.DateTimeInput(attrs={'type':'date'}, format=('%Y-%m-%d')),
            "hora_entrega": forms.DateTimeInput(attrs={'type':'time'}, format=('%H:%M')),
        }
        labels = {
            "fecha_entrega": "Fecha de entrega (Lunes a Sabado)",
            "hora_entrega": "Hora de entrega (10AM a 8PM)",
            "programar_diariamente" : "Programar entrega de Lunes a Viernes",
        }