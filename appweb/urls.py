from django.urls import path
from .views import *
from . import views



urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('menu/', menu, name="menu"),
    path('nosotros/', nosotros, name="nosotros"),
    path('login_usuario/', login_usuario, name='login_usuario'),
    path('registro/', registro_user, name='registro'),
    path('perfilAdm/', login_administrador, name="perfilAdministrador"),
    path('proveedor/', login_proveedor, name='perfilProveedor'),
    path('empresa/', login_empresa, name='perfilEmpresa'),
    path('registro_prod/', reg_prod, name='reg_prod'),
    path('registro_Proveedor/', reg_Proveedor, name='reg_Proveedor'),
    path('registro_Empresa/', reg_Empresa, name='reg_Empresa'),
    path('registro_prodProv/', reg_prodProveedor, name='reg_prodProveedor'),
    path('cart/', views.cart_view, name='cart_view'),
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('decrease_quantity/<int:cart_item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('increase_quantity/<int:cart_item_id>/', views.increase_quantity, name='increase_quantity'),
    path('shop/', views.compras, name='compras'),
    path('regUserEmpresa/', reg_user_Empresa, name='regUserEmpresa'),
    path('payment/', pago, name='payment'),
    path('perfilUser/', perfilUsuario, name='perfilUser'),
    path('perfilUserEmpresa/', perfilUsuarioEmpresa, name='perfilUserEmpresa'),
    path('aprobar-pedidos/<int:pedido_id>/', views.aprobar_pedidos, name='aprobar_pedidos'),
    path('rechazar-pedido/<int:pedido_id>/', views.rechazar_pedido, name='rechazar_pedido'),
    path('entregar-pedidos/<int:pedido_id>/', views.entregar_pedido, name='entregar_pedido'),
    path('modificar-producto/<int:producto_id>/', views.modificar_producto, name='modificar_producto'),
    path('eliminar-producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('modificar-proveedor/<int:proveedor_id>/', views.modificar_proveedor, name='modificar_proveedor'),
    path('eliminar-proveedor/<int:proveedor_id>/', views.eliminar_proveedor, name='eliminar_proveedor'),
    path('modificar-empresa/<int:empresa_id>/', views.modificar_empresa, name='modificar_empresa'),
    path('eliminar-empresa/<int:empresa_id>/', views.eliminar_empresa, name='eliminar_empresa'),
    path('modificar-usuario/<int:usuario_empresa_id>/', views.modificar_usuario_empresa, name='modificar_usuario'),
    path('eliminar-usuario-emp/<int:usuario_empresa_id>/', views.eliminar_usuario_empresa, name='eliminar_usuario'),

]