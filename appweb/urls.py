from django.urls import path
from .views import *



urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('menu/', menu, name="menu"),
    path('nosotros/', nosotros, name="nosotros"),
    path('login/', login_usuario, name='login'),
    path('registro/', registro_user, name='registro'),
]