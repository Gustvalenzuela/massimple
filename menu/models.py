from django.db import models

# Create your models here.

class Rol(models.Model):
    idRol = models.AutoField(primary_key = True, verbose_name='Id del Rol')
    nombreRol= models.CharField(max_length=30, verbose_name = 'Nombre del Rol', null=True, blank=False)


class Pregunta(models.Model):
    idPregunta = models.AutoField(primary_key = True, verbose_name='id de la Pregunta')
    nombrePregunta = models.CharField(max_length=30, verbose_name='Nombre de la Pregunta', null=True, blank=False)

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key = True, verbose_name= 'Id de la categoria')
    nombreCategoria = models.CharField(max_length=30, verbose_name='Nombre de las categoria', null= True, blank=False)



class Usuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True)
    rutUsuario = models.IntegerField()
    nombreUsuario = models.CharField(max_length=30)
    apellidoUsuario= models.CharField(max_length=30)
    telefonoUsuario= models.IntegerField()
    correoUsuario= models.CharField(max_length=40)
    claveUsuario= models.CharField(max_length=35)
    direccionUsuario= models.CharField(max_length= 50)
    respuestaUsuario= models.CharField(max_length= 100)
    pregunta= models.ForeignKey(Pregunta,on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True)
    nombreProducto = models.CharField(max_length=30, blank=False)
    descripcion = models.CharField(max_length=300, blank=False)
    marca = models.CharField(max_length=30, blank=False)
    stock = models.IntegerField()
    precio = models.IntegerField()
    fotoProducto = models.ImageField(upload_to="massimple", blank=False)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)




class Compra(models.Model):
    idCompra = models.AutoField(primary_key=True)
    estatus = models.CharField(max_length=50, blank=False)
    fEntrega = models.DateField()
    fCompra = models.DateField()
    total = models.IntegerField()
    carrito = models.CharField(max_length=60)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

class Detalle(models.Model):
    idDetalle = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()
    compra = models.ForeignKey(Compra,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
