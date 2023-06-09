from django.shortcuts import render,redirect
from .models import Producto, Categoria, Usuario, Rol, Compra, Pregunta, Detalle
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.




def principal (request):
    return render(request,'menu/principal.html')

def plantilla(request):
    return render(request, 'menu/plantilla.html')

def plantillaDetalle(request):
    return render(request, 'menu/plantillaDetalle.html')


def detergentes(request):
  
        return render(request,'menu/detergentes.html')
    

def productos(request):
    return render(request, 'menu/productos.html')

def proteccion(request):
    return render(request, 'menu/proteccion.html')

def iniciarSesion(request):
    logout(request)

    return render(request, 'menu/login.html' )
    

def cambiocontr(request):
    return render(request, 'menu/cambiocontr.html')

def Carrito(request):
    return render(request, 'menu/Carrito.html')

def Cloro(request):
    return render(request, 'menu/Cloro.html')

def crearcuenta(request):
    listaPreguntas = Pregunta.objects.all()
    contexto = {
        "preguntas": listaPreguntas
    }
    return render(request, 'menu/crearcuenta.html', contexto)

def EditarPerfil(request,id):
   
    usuario = Usuario.objects.get(rutUsuario=id)
    contexto = {
        "user":usuario
    }
    print(request.user.username)
    return render(request, 'menu/EditarPerfil.html',contexto)

def formEditarPerfil(request):
    #Accedemos al correo de la persona que se encuentra logeada
    correoUser = request.user.username
    cliente = Usuario.objects.get(correoUsuario = correoUser)
    
    
    run = cliente.rutUsuario
    print(run)
    #Se llaman a todos los usuarios registrador, con la finalidad de evitar
    #repeticiones en los correos electrónicos
    correos = User.objects.all()
    
    vNombre = request.POST['nombre']
    vCorreo = request.POST['correo']
    vFecha = request.POST.get('fecha',"")
    print(vCorreo)
    if vNombre != cliente.nombre:
       cliente.nombre = vNombre
       
    if vFecha != "":
        cliente.fechaUsuario = vFecha
        
    if vCorreo != cliente.correoUsuario:
        for correo in correos:
            if vCorreo.lower() == correo.username.lower():
                print("hola")
                messages.error(request, "Intente con otro correo")
                return redirect("EditarPerfil",id = run)
        
    cliente.correoUsuario = vCorreo
    userDjango = User.objects.get(username = correoUser)
    userDjango.username = vCorreo
    clave = userDjango.password
    cliente.save()
    userDjango.save()
    userDjango = authenticate(username = vCorreo,password = clave)
    login(request, userDjango)
    
    #Debido a que, la vista perfilusuario recibe un parámetro,
    #dentro del redirect le adjuntamos el run del cliente
    return redirect("perfilusuario",id = run)
def Herramientas(request):

    return render(request, 'menu/Herramientas.html')

def listado(request):
    lista = Producto.objects.all()
    contexto = {
        "productos": lista
    }
    return render(request, 'menu/listado.html', contexto)

def Otros(request):
    return render(request, 'menu/Otros.html')


def perfiladmin(request):
    lista = Usuario.objects.all()
    contexto = {
        "usuarios": lista
    }
    return render(request, 'menu/perfiladmin.html', contexto)

def perfilusuario(request, id):
    lista = Usuario.objects.get( rutUsuario = id)
    contexto = {
        "usuarios": lista
    }
    print(request.user.is_authenticated)
    
    return render(request, 'menu/perfilusuario.html', contexto)

def recuperar(request):
    return render(request, 'menu/recuperar.html')

def DetalleMasimple(request):
    return render(request, 'menu/DetalleMasimple.html')

def DlavalozaLim(request):
    return render(request,'menu/D.lavalozaLim.html')

def detalleCloroL(request):
    return render(request, 'menu/detalleCloroL.html')

def detalleGuan(request):
    return render(request, 'menu/detalleGuan.html')

def Dherra1(request):
    return render(request, 'menu/D.herra1.html')

def Dotro1(request):
    return render(request, 'menu/D.otro1.html')

def anadirp(request):
    listaCategorias = Categoria.objects.all()
    contexto = {

        "categorias": listaCategorias

    }

    return render(request, 'menu/anadirp.html', contexto)

def modificarP(request, id):
    categorias = Categoria.objects.all()
    producto = Producto.objects.get(idProducto = id)
    contexto = {
        "lista_categorias": categorias,
        "datos": producto
    }
    
    return render(request,'menu/modificarP.html', contexto)

def formProducto(request):
    
    vNombre = request.POST['nombre']
    vDescripcion = request.POST['descripcion']
    vMarca = request.POST['marca']
    vStock = request.POST['stock']
    vPrecio = request.POST['precio']
    
    vFoto = request.FILES['foto']
    vCategoria = request.POST['categoria']

    vRegistroCategoria = Categoria.objects.get(idCategoria = vCategoria)
    Producto.objects.create( nombreProducto = vNombre, descripcion = vDescripcion, marca = vMarca, stock = vStock, precio = vPrecio, fotoProducto = vFoto, categoria = vRegistroCategoria)

    messages.success(request, 'Producto añadido!')
    return redirect('anadirp')

def formUsuario(request):
    vRut = request.POST['rut']
    vDv = request.POST['dv']
    vNombreU = request.POST['nombre']
    vApellido = request.POST['apellido']
    vTelefono = request.POST['telefono']
    vCorreo = request.POST['email']
    vFecha = request.POST['fecha']
    vContra = request.POST['password']
    vRespuesta = request.POST['respuesta']
    vPregunta = request.POST['pregunta']
    vRol = 1
    
    vRegistroRol = Rol.objects.get(idRol = vRol)
    vRegistroPregunta = Pregunta.objects.get(idPregunta = vPregunta)
    Usuario.objects.create(rutUsuario = vRut,dv = vDv ,nombre = vNombreU, apellido = vApellido, 
                            telefonoUsuario= vTelefono,
                            correoUsuario = vCorreo, fechaUsuario= vFecha, claveUsuario= vContra, 
                            respuestaUsuario = vRespuesta, pregunta = vRegistroPregunta, 
                            rol = vRegistroRol )
    user = User.objects.create_user(vCorreo,vCorreo,vContra)
    return redirect('crearcuenta')


def eliminarProducto(request, id):
    producto = Producto.objects.get(idProducto = id)
    producto.delete()

    messages.success(request, 'El producto a sido eliminado')
    return redirect('listado')

def modificarProducto(request):
    idM = request.POST['idProducto']
    nombreM = request.POST['nombre']
    descripcionM = request.POST['descripcion']
    marcaM = request.POST['marca']
    stockM = request.POST['stock']
    precioM = request.POST['precio']
    fotoM = request.FILES['foto']
    categoriaM = request.POST['categoria']

    producto = Producto.objects.get(idProducto = idM)
    producto.nombreProducto = nombreM
    producto.descripcion = descripcionM
    producto.marca = marcaM
    producto.stock = stockM
    producto.precio = precioM
    producto.fotoProducto = fotoM
    
    registroCategoria = Categoria.objects.get(idCategoria = categoriaM)
    producto.categoria = registroCategoria
    messages.success(request, 'El producto a sido modificado')
    producto.save()
   
    return redirect('listado')
    


def iniciosesion (request):
    usuario1 = request.POST['correo']
    contrasenia1 = request.POST['palabraSecreta']
    print(usuario1)
    print(contrasenia1)
    

    try:
        user1= User.objects.get(username = usuario1)
    except User.DoesNotExist:
        messages.error(request, 'El usuario ingresado no existe')
        return redirect('login')
    
    pass_valida= check_password(contrasenia1, user1.password)
    if not pass_valida:
        messages.error(request,'El usuario o la contraseña son incorrectos')
        return redirect('login')
    
    usuario2 = Usuario.objects.get(correoUsuario=usuario1, claveUsuario=contrasenia1)
    user = authenticate(username=usuario1, password=contrasenia1)
    print(user)
    if user is not None:
        
        
        if (usuario2.rol.idRol == 2) :
            login(request,user) 
            return redirect ('perfiladmin')
        
        if (usuario2.rol.idRol == 1):
            login(request, user)
            run = usuario2.rutUsuario
            return redirect('perfilusuario',id=run)
        
        else:
            contexto = {"usuario": usuario2}
            return render(request, 'menu/perfilusuario.html', contexto)
        
        

def cerrarSesion(request):
    logout(request)
    return redirect('login')

   