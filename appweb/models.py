from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.CharField(max_length=10)
    asunto = models.CharField(max_length=50)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
    
list_tipo_producto = [
    (0, 'Entrada'),
    (1, 'Principal'),
    (2, 'Postre'),
    (3, 'Liquidos')

] 

list_disponibilidad_producto = [
    (0, 'Disponible'),
    (1, 'No Disponible')
]

list_origen_producto = [
    (0, 'Propio'),
    (1, 'Proveedor Externo')
]
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio = models.IntegerField()
    imagen = models.ImageField(upload_to='producto', null=False)
    tipo_plato = models.IntegerField(choices=list_tipo_producto)
    disponible = models.IntegerField(choices=list_disponibilidad_producto)
    origen = models.IntegerField(choices=list_origen_producto)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    cantidadVendidos = models.IntegerField(default=0)


    def __str__(self):
        return self.nombre

class CartItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    total_item = models.PositiveIntegerField()
    total_carrito = models.PositiveIntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

list_estado_usuarioEmpresa = [
    (0, 'Activo'),
    (1, 'Desactivado')
]

class usuarioEmpresa(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    contrasena = models.CharField(max_length=50)
    saldo = models.IntegerField(default=0)
    empresa = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    estado = models.IntegerField(choices=list_estado_usuarioEmpresa, default=0)

    def __str__(self):
        return self.nombre
    
list_estado_pedido = [
    (0, 'Pendiente'),
    (1, 'En Camino'),
    (2, 'Cancelado'),
    (3, 'Entregado')
]

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    total = models.IntegerField()
    programar_diariamente = models.BooleanField(default=False)
    fecha_entrega = models.DateField(null=True, blank=True)
    hora_entrega = models.TimeField(null=True, blank=True)
    estado = models.IntegerField(choices=list_estado_pedido, default=0)
    detalle_pedido = models.ManyToManyField('CartItem')

    def __str__(self):
        return f"Pedido #{self.pk} - Usuario: {self.usuario.username}"
    

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    total_item = models.PositiveIntegerField()

    def __str__(self):
        return f"Detalle #{self.pk} - Pedido #{self.pedido.pk}"