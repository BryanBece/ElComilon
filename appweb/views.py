from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.


def home(request):
    return render(request, 'home.html')

def contacto(request):

    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto guardado"
        else:
            data["form"] = formulario
            data["mensaje"] = "Error al enviar, intente nuevamente"

    return render(request, 'contacto.html', data)