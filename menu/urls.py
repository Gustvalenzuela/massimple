from django.contrib import admin
from django.urls import path

from .views import plantilla,plantillaDetalle,cerrarSesion,iniciosesion,formUsuario,modificarProducto,eliminarProducto,modificarP,formProducto,principal,detergentes,productos, proteccion,login,cambiocontr,Carrito,crearcuenta,EditarPerfil,Herramientas,listado,Otros,perfiladmin,perfilusuario,recuperar,DlavalozaLim,Cloro,detalleCloroL,DetalleMasimple,detalleGuan, Dherra1, Dotro1,anadirp
from .views import iniciarSesion,formEditarPerfil
urlpatterns = [
    path('',principal,name="inicio"),
    path('paginadetergentes',detergentes,name="detergentes"),
    path('productosAseo',productos, name="productos"),
    path('paginaproteccion',proteccion,name="proteccion"),
    path('paginalogin',iniciarSesion,name="login"),
    path('cambiocontr',cambiocontr,name="cambiocontr"),
    path('Carrito', Carrito,name="Carrito"),
    path('Cloro',Cloro,name="Cloro"),
    path('crearcuenta',crearcuenta,name="crearcuenta"),
    path('EditarPerfil/<int:id>',EditarPerfil,name="EditarPerfil"),
    path('Herramientas',Herramientas,name="Herramientas"),
    path('listado',listado,name="listado"),
    path('Otros',Otros,name="Otros"),
    path('perfiladmin',perfiladmin,name="perfiladmin"),
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
    path('eliminarProducto/<int:id>', eliminarProducto, name="eliminarProducto"),
    path('modificarProducto', modificarProducto, name="modificarProducto"),
    path('iniciosesion', iniciosesion, name="iniciosesion"),
    path('cerrarSesion', cerrarSesion, name="cerrarSesion"),
    path('plantillaDetalle', plantillaDetalle, name="plantillaDetalle"),
    path('plantilla', plantilla, name="plantilla"),
    #Forms
    path('formUsuario', formUsuario, name="formUsuario"),
    path('formProducto', formProducto, name="formProducto"),
    path('formEditarPerfil', formEditarPerfil, name="formEditarPerfil"),

]
