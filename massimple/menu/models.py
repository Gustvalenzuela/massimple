from django.db import models

# Create your models here.

class Rol(models.Model):
    idRol = models.AutoField(primary_key = True, verbose_name='Id del Rol')
    nombreRol= models.CharField(max_length=80, verbose_name = 'Nombre del Rol', null=True, blank=False)

    def __str__(self)-> str:
        return self.nombreRol

class Pregunta(models.Model):
    idPregunta = models.AutoField(primary_key = True, verbose_name='id de la Pregunta')
    nombrePregunta = models.CharField(max_length=100, verbose_name='Nombre de la Pregunta', null=True, blank=False)

    def __str__(self) -> str:
        return self.nombrePregunta

class Categoria(models.Model):
    idCategoria = models.AutoField(primary_key = True, verbose_name= 'Id de la categoria')
    nombreCategoria = models.CharField(max_length=30, verbose_name='Nombre de las categoria', null= True, blank=False)
    def __str__(self) -> str:
        return self.nombreCategoria



class Usuario(models.Model):
    rutUsuario = models.IntegerField(primary_key=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    telefonoUsuario= models.IntegerField()
    correoUsuario= models.CharField(max_length=80)
    fechaUsuario = models.DateField()
    claveUsuario= models.CharField(max_length=35)
    respuestaUsuario= models.CharField(max_length= 100)
    pregunta= models.ForeignKey(Pregunta,on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre

class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombreProducto = models.CharField(max_length=30, blank=False)
    descripcion = models.TextField(max_length=300, blank=False)
    marca = models.CharField(max_length=30, blank=False)
    stock = models.IntegerField()
    precio = models.IntegerField()
    fotoProducto = models.ImageField(upload_to="massimple", blank=False)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)

    def str(self)-> str:
        return self.nombreProducto

class Compra(models.Model):
    idCompra = models.AutoField(primary_key=True)
    fEntrega = models.DateField()
    fCompra = models.DateField()
    total = models.IntegerField()
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def str(self)-> str:
        return str(self.idCompra)

class Detalle(models.Model):
    idDetalle = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    subtotal = models.IntegerField()
    compra = models.ForeignKey(Compra,on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)

class Carrito(models.Model):
    id = models.AutoField(primary_key=True)
    run_cliente = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_creacion = models.DateField()
    estado = models.CharField(max_length=25)
    fecha_compra = models.DateField()
    
    def __str__(self) -> str:
        return str(self.run_cliente)

