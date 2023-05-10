from django.contrib import admin
from django.urls import path

from .views import principal,detergentes

urlpatterns = [
    path('',principal,name="inicio"),
    path('paginadetergentes',detergentes,name="detergentes"),
]
