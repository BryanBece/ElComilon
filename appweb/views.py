from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, User
from django.urls import reverse



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
            messages.success(request, "Mensaje enviado")
        else:
            data["form"] = formulario
            messages.error(request, "Error al enviar el mensaje")

    return render(request, 'contacto.html', data)

def menu(request):
    producto = Producto.objects.all()

    data = {
        'producto': producto
    }

    return render(request, 'menu.html', data)

def nosotros(request):
    return render(request, 'nosotros.html')


def login_usuario(request):
    messages.success(request, "Bienvenido")
    return redirect('home')

def registro_user(request):
    
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        correo = request.POST.get("correo")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            print("Las contraseñas no coinciden.")
        elif User.objects.filter(email=correo).exists():
            messages.error(request, "El correo ya está registrado.")
            print("El correo ya está registrado.")
        else:
            usu = User()
            usu.set_password(password1)
            usu.email = correo
            usu.username = nombre
            usu.first_name = nombre
            usu.last_name = apellido
            grupo = Group.objects.get(name="Usuario") # Cambiar a Artista si se quiere crear un artista
            
            try:
                usu.save()
                usu.groups.add(grupo)
                messages.success(request, "Usuario creado correctamente.")
                print("Usuario creado correctamente.")
                return redirect(reverse("home"))
            except:
                messages.error(request, "Error al crear el usuario.")
                print("Error al crear el usuario.")
    
    return render(request, "registration/register.html")
