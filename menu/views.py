from django.shortcuts import render,redirect
from .models import Producto, Categoria
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
    usuario1 = request.POST['usuario']#fromulario
    contra1 = request.POST['contra']
    try: 
        user1 = User.objects.get(username = usuario1)
    except User.DoesNotExist:
        messages.error(request, 'El usuario o la contraseña son incorrectos')
        return redirect('inicio')

    pass_valida = check_password(contra1, user1.password)
    if not pass_valida:
        messages.error(request,'El usuario o la contraseña son incorrectos')
        return redirect('inicio')

    usuario2 = Usuario.objects.get(username = usuario1, contrasennia = contra1)
    user = authenticate(username=usuario1, password=contra1)
    if user is not None:
        login(request, user)
        if( usuario2.tipousuario.idTipoUsuario == 1):
            return redirect('menu_admin')
        else:
            conexto = ("usuario":usuario2)

            return render(request, 'menu/principal.html', contexto)
    

def cambiocontr(request):
    return render(request, 'menu/cambiocontr.html')

def Carrito(request):
    return render(request, 'menu/Carrito.html')

def Cloro(request):
    return render(request, 'menu/Cloro.html')

def crearcuenta(request):
    user = User.objects.create_user("vale", "vale@gmail.com", "contradevale")

    return render(request, 'menu/crearcuenta.html')

def EditarPerfil(request):
    return render(request, 'menu/EditarPerfil.html')

def Herramientas(request):
    return render(request, 'menu/Herramientas.html')

def listado(request):
    return render(request, 'menu/listado.html')

def Otros(request):
    return render(request, 'menu/Otros.html')

def perfiladmin(request):
    return render(request, 'menu/perfiladmin')

def perfilusuario(request):
    return render(request, 'menu/perfilusuario')

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

def modificarP(request):
    
    return render(request,'menu/modificarP.html')

def formProducto(request):
    vId = request.POST['idProducto']
    vNombre = request.POST['nombre']
    vDescripcion = request.POST['descripcion']
    vMarca = request.POST['marca']
    vStock = request.POST['stock']
    vPrecio = request.POST['precio']
    
    vFoto = request.FILES['foto']
    vCategoria = request.POST['categoria']

    vRegistroCategoria = Categoria.objects.get(idCategoria = vCategoria)
    Producto.objects.create(idProducto = vId, nombreProducto = vNombre, descripcion = vDescripcion, marca = vMarca, stock = vStock, precio = vPrecio, fotoProducto = vFoto, categoria = vRegistroCategoria)

    
    return redirect('anadirp')
