from django.contrib import admin
from django.urls import path

from .views import principal,detergentes,productos,proteccion,login

urlpatterns = [
    path('',principal,name="inicio"),
    path('paginadetergentes',detergentes,name="detergentes"),
    path('paginadeproductos',productos,name="productos"),
    path('paginaproteccion',proteccion,name="proteccion"),
    path('paginalogin',login,name="login"),


]
