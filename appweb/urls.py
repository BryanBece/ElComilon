from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('home/', home, name="home"),
    path('contacto/', contacto, name="contacto"),
]