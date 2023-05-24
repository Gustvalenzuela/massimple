from django.contrib import admin
from .models import Rol, Pregunta, Categoria, Usuario, Producto, Compra, Detalle

# Register your models here.
admin.site.register(Rol)
admin.site.register(Pregunta)
admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(Compra)
admin.site.register(Detalle)
