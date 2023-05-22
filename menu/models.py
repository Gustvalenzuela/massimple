from django.db import models

# Create your models here.

class Rol(models.Model):
    idRol = models.AutoField(primari_key = True, verbose_name='Id del Rol')
    nombreRol= models.CharField(max_length=30, verbose_name = 'Nombre del Rol', null=True, blank=False)


class Pregunta(models.Model):
    idPregunta = models.AutoField(primari_key = True, verbose_name='id de la Pregunta')
    nombrePregunta = models.CharField(max_length=30, verbose_name='Nombre de la Pregunta', null=True, blank,False)

class Categoria(models.Model):
    idCategoria = models.IntergerField(primari_key = True, verbose_name= 'Id de la categoria')
    nombreCategoria = models.CharField(max_length=30, verbose_name='Nombre de las categoria', null= True, blank=False)



class Usuario(models.Model):
    idUsuario = models.IntergerField(primary_key=True)
    rutUsuario = models.IntergerField()
    nombreUsuario = models.CharField(max_length=30)
    apellidoUsuario= models.CharField(max_length=30)
    telefonoUsuario= models.IntergerField()
    correoUsuario= models.CharField(max_length=40)
    claveUsuario= models.CharField(max_length=35)
    direccionUsuario= models.CharField(max_legth= 50)
    respuestaUsuario= models.ChardField(max_length= 100)
    pregunta= models.ForeignKey(Pregunta,on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)