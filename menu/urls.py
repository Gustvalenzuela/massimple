from django.contrib import admin
from django.urls import path

from .views import principal,detergentes,productos, proteccion,login,cambiocontr,Carrito,crearcuenta,EditarPerfil,Herramientas,listado,Otros,perfiladmin,perfilusuario,recuperar,DlavalozaLim

urlpatterns = [
    path('',principal,name="inicio"),
    path('paginadetergentes',detergentes,name="detergentes"),
    path('productosAseo',productos, name="productos"),
    path('paginaproteccion',proteccion,name="proteccion"),
    path('paginalogin',login,name="login"),
    path('cambiocontr',cambiocontr,name="cambiocontr"),
    path('Carrito', Carrito,name="Carrito"),
    path('crearcuenta',crearcuenta,name="crearcuenta"),
    path('EditarPerfil',EditarPerfil,name="EditarPerfil"),
    path('Herramientas',Herramientas,name="Herramientas"),
    path('listado',listado,name="listado"),
    path('Otros',Otros,name="Otros"),
    path('perfiladmin',perfiladmin,name="perfiladmin"),
    path('perfilusuario',perfilusuario,name="perfilusuario"),
    path('recuperar',recuperar,name="recuperar"),
    path('DlavalozaLim',DlavalozaLim, name="DlavalozaLim",)
    

    
    
    
    
]
