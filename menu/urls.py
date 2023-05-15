from django.contrib import admin
from django.urls import path

from .views import principal,detergentes,productos

urlpatterns = [
    path('',principal,name="inicio"),
    path('paginadetergentes',detergentes,name="detergentes"),
    path('paginadeproductos',productos,name="productos"),

]
