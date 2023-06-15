from django.contrib import admin
from django.urls import path

from .views import formSesion,formUsuario,modificarProducto,eliminarProducto,modificarP,formProducto,principal,detergentes,productos, proteccion,login,cambiocontr,Carrito,crearcuenta,EditarPerfil,Herramientas,listado,Otros,perfiladmin,perfilusuario,recuperar,DlavalozaLim,Cloro,detalleCloroL,DetalleMasimple,detalleGuan, Dherra1, Dotro1,anadirp

urlpatterns = [
    path('',principal,name="inicio"),
    path('paginadetergentes',detergentes,name="detergentes"),
    path('productosAseo',productos, name="productos"),
    path('paginaproteccion',proteccion,name="proteccion"),
    path('paginalogin',login,name="login"),
    path('cambiocontr',cambiocontr,name="cambiocontr"),
    path('Carrito', Carrito,name="Carrito"),
    path('Cloro',Cloro,name="Cloro"),
    path('crearcuenta',crearcuenta,name="crearcuenta"),
    path('EditarPerfil',EditarPerfil,name="EditarPerfil"),
    path('Herramientas',Herramientas,name="Herramientas"),
    path('listado',listado,name="listado"),
    path('Otros',Otros,name="Otros"),
    path('perfiladmin/<int:id>',perfiladmin,name="perfiladmin"),
    path('perfilusuario/<int:id>',perfilusuario,name="perfilusuario"),
    path('recuperar',recuperar,name="recuperar"),
    path('DetalleMasimple', DetalleMasimple, name="DetalleMasimple"),
    path('DlavalozaLim',DlavalozaLim, name="DlavalozaLim"),
    path('detalleCloroL', detalleCloroL, name="detalleCloroL"),
    path('detalleGuan', detalleGuan, name="detalleGuan"),
    path('Dherra1', Dherra1, name="Dherra1"),
    path('Dotro1', Dotro1, name="Dotro1"),
    path('anadirp', anadirp, name="anadirp"),
    path('modificarP/<int:id>', modificarP, name="modificarP"),
    path('formProducto', formProducto, name="formProducto"),
    path('eliminarProducto/<int:id>', eliminarProducto, name="eliminarProducto"),
    path('modificarProducto', modificarProducto, name="modificarProducto"),
    path('formUsuario', formUsuario, name="formUsuario"),
    path('formSesion', formSesion, name="formSesion"),
    
    

    
    
    
    
]
