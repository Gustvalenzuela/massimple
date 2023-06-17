from django.shortcuts import render,redirect
from .models import Producto, Categoria, Usuario, Rol, Compra, Pregunta, Detalle
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login, logout

# Create your views here.




def principal (request):
    return render(request,'menu/principal.html')


def detergentes(request):
    return render(request,'menu/detergentes.html')

def productos(request):
    return render(request, 'menu/productos.html')

def proteccion(request):
    return render(request, 'menu/proteccion.html')

def login(request):
    

    return render(request, 'menu/login.html', )
    

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

def EditarPerfil(request):
    return render(request, 'menu/EditarPerfil.html')

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
    return render(request, 'menu/perfiladmin.html')

def perfilusuario(request):
    
    return render(request, 'menu/perfilusuario.html')

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

    
    return redirect('anadirp')

def formUsuario(request):
    vRut = request.POST['rut']
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
    Usuario.objects.create(rutUsuario = vRut, nombreUsuario = vNombreU, apellidoUsuario = vApellido, telefonoUsuario= vTelefono,
                            correoUsuario = vCorreo, fechaUsuario= vFecha, claveUsuario= vContra, respuestaUsuario = vRespuesta, pregunta = vRegistroPregunta, rol = vRegistroRol )

    return redirect('crearcuenta')


def eliminarProducto(request, id):
    producto = Producto.objects.get(idProducto = id)
    producto.delete()
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

    producto.save()
    return redirect('listado')

def inicioSesion(request):
    try:
        vCorreo = request.POST['correo']
        vContra = request.POST['palabraSecreta']
        vRol = 0
        vRun= 0
        registro = Usuario.objects.all()


        for rol in registro:
            if rol.correoUsuario == vCorreo and rol.claveUsuario == vContra:

                    vRun = rol.idUsuario
                    vRol = rol.rol.idRol
        user1 = User.objects.get(username = vCorreo)
        print(user1.username)
        pass_valida = check_password(vContra,user1.password)

        if not pass_valida:
            messages.error(request,"El usuario o la contraseña son incorrectos")
            return redirect('login')

        user = authenticate(username=vCorreo,password = vContra)

        print(user)
        if user is not None:
            if vRol == 1:
                login(request,user)
                return redirect(f'perfilusuario{vRun}')


            if vRol == 2:
                login(request,user)
                return redirect('perfiladmin') 

            if vRol == 0:
                messages.success(request, "Usuario no registrado")
                return redirect('login')
    except User.DoesNotExist:
            messages.error(request,"El usuario no existe")
            return redirect('login')
    except Exception as e:
        print(e)
