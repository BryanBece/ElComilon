from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import F, Sum


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
    if request.user.groups.filter(name="Usuario"):
        messages.success(request, f"Bienvenido {request.user.username}")
        return redirect("perfilUser")
    elif request.user.groups.filter(name="Proveedor"):
        messages.success(request, f"Bienvenido {request.user.username}")
        return redirect("perfilProveedor")
    elif request.user.groups.filter(name="Administrador"):
        messages.success(request, f"Bienvenido {request.user.username}")
        return redirect("perfilAdministrador")
    elif request.user.groups.filter(name="Empresa"):
        messages.success(request, f"Bienvenido {request.user.username}")
        return redirect("perfilEmpresa")
    elif request.user.groups.filter(name="Usuario_empresa"):
        messages.success(request, f"Bienvenido {request.user.username}")
        return redirect("perfilUserEmpresa")
    
    
    return redirect(to="home")

def login_administrador(request):
    Pedidos = Pedido.objects.all()
    Productos = Producto.objects.all()
    Proveedores = User.objects.filter(groups__name="Proveedor")
    Empresas = User.objects.filter(groups__name="Empresa")
    detaPed = DetallePedido.objects.all()
    data = {
        'ped': Pedidos,
        'prod': Productos,
        'prov': Proveedores,
        'emp': Empresas,
        'detaPed': detaPed
    }
    return render(request, 'perfilAdmin.html', data)

def login_proveedor(request):
    Productos = Producto.objects.all()
    data = {
        'prod': Productos
    }
    return render(request, 'perfilProveedor.html', data)

def login_empresa(request):
    # Mostrar usuarios de la empresa
    usuarios = User.objects.filter(groups__name="Usuario_empresa")
    user_empresas = usuarioEmpresa.objects.all()
    data = {
        'usu': usuarios,
        'usuEmp': user_empresas
    }

    # Asignar nuevo saldo
    if request.method == "POST":
        saldo = request.POST.get("saldo")
        user_id = request.POST.get("id")
        try:
            # Actualizar el saldo del usuario
            user = User.objects.get(id=user_id)
            user_emp = usuarioEmpresa.objects.get(empresa=user)
            user_emp.saldo = int(saldo)
            user_emp.save()
            messages.success(request, "Saldo actualizado correctamente.")
        except (User.DoesNotExist, usuarioEmpresa.DoesNotExist):
            print(user_id, saldo)
            messages.error(request, "Usuario o empresa no encontrados.")
            return redirect(reverse("perfilEmpresa"))

    return render(request, 'perfilEmpresa.html', data)

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
            grupo = Group.objects.get(name="Usuario")
            
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

@login_required(login_url='/accounts/login')
def reg_prod(request):
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        
        if formulario.is_valid():
            prod = Producto()
            autor = request.user
            prod.autor = autor
            formulario.save()
            messages.success(request, "Producto registrado")
        else:
            data["form"] = formulario
            messages.error(request, "Error al registrar el producto")


    return render(request, "registration/registroProductoAdmin.html", data)

@login_required(login_url='/accounts/login')
def reg_prodProveedor(request):
    data = {
        'form': ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        
        if formulario.is_valid():
            prod = Producto()
            autor = request.user
            prod.autor = autor
            formulario.save()
            messages.success(request, "Producto registrado")
        else:
            data["form"] = formulario
            messages.error(request, "Error al registrar el producto")


    return render(request, "registration/registroProductoProveedor.html", data)

@login_required(login_url='/accounts/login')
def reg_Proveedor(request):
        
        if request.method == "POST":
            nombre = request.POST.get("nombre")
            rut = request.POST.get("rut")
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
                usu.last_name = rut
                grupo = Group.objects.get(name="Proveedor")
                
                try:
                    usu.save()
                    usu.groups.add(grupo)
                    messages.success(request, "Usuario creado correctamente.")
                    print("Usuario creado correctamente.")
                    return redirect(("perfilAdministrador"))
                except:
                    messages.error(request, "Error al crear el usuario.")
                    print("Error al crear el usuario.")
    
        return render(request, "registration/registroProveedor.html")

@login_required(login_url='/accounts/login')
def reg_Empresa(request):
        
        if request.method == "POST":
            nombre = request.POST.get("nombre")
            rutEmpresa = request.POST.get("rutEmpresa")
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
                usu.last_name = rutEmpresa
                grupo = Group.objects.get(name="Empresa")
                
                try:
                    usu.save()
                    usu.groups.add(grupo)
                    messages.success(request, "Usuario creado correctamente.")
                    print("Usuario creado correctamente.")
                    return redirect(("perfilAdministrador"))
                except:
                    messages.error(request, "Error al crear el usuario.")
                    print("Error al crear el usuario.")
    
        return render(request, "registration/registroEmpresa.html")

#Carrito de compra

def cart_view(request):
    cart_items = CartItem.objects.filter(usuario=request.user)
    total_items = cart_items.aggregate(Sum('total_item'))['total_item__sum']
    total_carrito = cart_items.aggregate(Sum('total_carrito'))['total_carrito__sum']
    return render(request, 'carritoCompras.html', {'cart_items': cart_items, 'total_items': total_items, 'total_carrito': total_carrito})

def add_to_cart(request, product_id):
    product = Producto.objects.get(pk=product_id)
    cart_item, created = CartItem.objects.get_or_create(
        producto=product,
        usuario=request.user,
        defaults={'cantidad': 1, 'total_item': product.precio, 'total_carrito': product.precio}
    )
    if not created:
        cart_item.cantidad += 1
        cart_item.total_item = cart_item.cantidad * product.precio
        cart_item.total_carrito += product.precio
        cart_item.save()
    messages.success(request, "Producto agregado al carrito")
    return redirect('compras')

def increase_quantity(request, cart_item_id):
    product = Producto.objects.get(pk=cart_item_id)
    cart_item, created = CartItem.objects.get_or_create(
        producto=product,
        usuario=request.user,
        defaults={'cantidad': 1, 'total_item': product.precio, 'total_carrito': product.precio}
    )
    if not created:
        cart_item.cantidad += 1
        cart_item.total_item = cart_item.cantidad * product.precio
        cart_item.total_carrito += product.precio
        cart_item.save()
    messages.success(request, "Producto agregado al carrito")
    return redirect('cart_view')

def decrease_quantity(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)

    if cart_item.cantidad > 1:
        cart_item.cantidad -= 1
        cart_item.total_item -= cart_item.producto.precio
        cart_item.total_carrito -= cart_item.producto.precio
        cart_item.save()
        messages.success(request, "Cantidad del producto disminuida")
    else:
        cart_item.delete()
        messages.success(request, "Producto eliminado del carrito")

    return redirect('cart_view')

def remove_from_cart(request, cart_item_id):
    cart_item = CartItem.objects.get(id=cart_item_id)
    cart_item.delete()
    messages.success(request, "Producto eliminado del carrito")
    return redirect('cart_view')

#Fin Carrito de compra

@login_required(login_url='/accounts/login')
def compras(request):
    producto = Producto.objects.all()

    data = {
        'producto': producto
    }

    return render(request, 'compras.html', data)

@login_required(login_url='/accounts/login')
def reg_user_Empresa(request):
    userEmp = usuarioEmpresaForm()
    data = {
        'form': userEmp
    }

    if request.method == 'POST':
        form = usuarioEmpresaForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            apellido = form.cleaned_data.get('apellido')
            correo = form.cleaned_data.get('correo')
            contrasena = form.cleaned_data.get('contrasena')
            saldo = form.cleaned_data.get('saldo')
            grupo = Group.objects.get(name="Usuario_empresa")
            

            if User.objects.filter(email=correo).exists():
                    messages.error(request, "El correo ya está registrado.")
                    return redirect('reg_user_Empresa')

            usu = User.objects.create_user(username=nombre, email=correo, password=contrasena, first_name=nombre, last_name=apellido)
            usuEmpresa = usuarioEmpresa.objects.create(saldo=saldo, nombre=nombre, apellido=apellido, correo=correo, empresa=usu)
            usuEmpresa.save()

            usu.groups.add(grupo)

            messages.success(request, "Usuario creado correctamente.")
            print("Usuario creado correctamente.")
            return redirect("perfilEmpresa")
        else:
            messages.error(request, "Error al crear el usuario.")
            print("Error al crear el usuario.")

    return render(request, 'registration/registroUsuarioEmpresa.html', data)

@login_required(login_url='/accounts/login')
def pago(request):
    form = pedidoForm()
    cart_items = CartItem.objects.filter(usuario=request.user)
    total_carrito = cart_items.aggregate(Sum('total_carrito'))['total_carrito__sum']

    # Obtener el grupo "Usuario_empresa"
    grupo_usuario_empresa = Group.objects.get(name='Usuario_empresa')

    if request.method == 'POST':
        form = pedidoForm(request.POST)
        if form.is_valid():
            if grupo_usuario_empresa in request.user.groups.all():
                usuario_empresa = usuarioEmpresa.objects.get(empresa=request.user)

                if usuario_empresa.saldo >= total_carrito:
                    usuario_empresa.saldo -= total_carrito
                    usuario_empresa.save()
                    pedido = form.save(commit=False)
                    pedido.usuario = request.user
                    pedido.total = total_carrito
                    pedido.save()

                    # Guardar el detalle del pedido
                    for cart_item in cart_items:
                        detalle_pedido = DetallePedido(
                            pedido=pedido,
                            producto=cart_item.producto,
                            cantidad=cart_item.cantidad,
                            total_item=cart_item.total_item
                        )
                        detalle_pedido.save()
                        producto = cart_item.producto
                        Producto.objects.filter(id=producto.pk).update(cantidadVendidos=F('cantidadVendidos') + cart_item.cantidad)

                    cart_items.delete()
                    messages.success(request, "Pedido realizado correctamente.")
                    return redirect('compras')
                else:
                    messages.error(request, "Saldo insuficiente.")

            else:
                pedido = form.save(commit=False)
                pedido.usuario = request.user
                pedido.total = total_carrito
                pedido.save()

                # Guardar el detalle del pedido
                for cart_item in cart_items:
                    detalle_pedido = DetallePedido(
                        pedido=pedido,
                        producto=cart_item.producto,
                        cantidad=cart_item.cantidad,
                        total_item=cart_item.total_item
                    )
                    detalle_pedido.save()
                    producto = cart_item.producto
                    Producto.objects.filter(id=producto.pk).update(cantidadVendidos=F('cantidadVendidos') + cart_item.cantidad)

                cart_items.delete()
                messages.success(request, "Pedido realizado correctamente.")
                return redirect('compras')

    return render(request, 'pago.html', {'cart_items': cart_items, 'total_carrito': total_carrito, 'form' : form})

@login_required(login_url='/accounts/login')
def perfilUsuario (request):
    #Mostrar pedidos del usuario
    pedidos = Pedido.objects.filter(usuario=request.user)
    data = {
        'ped': pedidos
    }
    return render(request, 'perfilUsuario.html', data)

@login_required(login_url='/accounts/login')
def perfilUsuarioEmpresa (request):
    #Mostrar pedidos del usuario
    pedidos = Pedido.objects.filter(usuario=request.user)
    usu = usuarioEmpresa.objects.get(empresa=request.user)
    data = {
        'ped': pedidos,
        'usu': usu
    }
    return render(request, 'perfilUsuarioEmpresa.html', data)

def aprobar_pedidos(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    print(pedido)
    print(pedido.estado)
    pedido.estado = 1
    print(pedido.estado)
    pedido.save()
    messages.success(request, 'El pedido ha sido aprobado')
    return redirect('perfilAdministrador')
    
def rechazar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.estado = 2
    pedido.save()
    messages.success(request, 'El pedido ha sido rechazado exitosamente.')
    return redirect('perfilAdministrador')