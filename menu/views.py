from django.shortcuts import render,redirect
from .models import Producto, Categoria

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
    return render(request, 'menu/login.html')

def cambiocontr(request):
    return render(request, 'menu/cambiocontr.html')

def Carrito(request):
    return render(request, 'menu/Carrito.html')

def Cloro(request):
    return render(request, 'menu/Cloro.html')

def crearcuenta(request):
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

def formProducto(request):
    vId: request.POST['idProducto']
    vNombre: request.POST['nombre']
    vDescripcion: request.POST['descripcion']
    vMarca: request.POST['marca']
    vStock: request.POST['stock']
   
    vPrecio: request.POST['precio']
    
    vFoto: request.FILE['foto']
    vCategoria: request.POST['categoria']

    vRegistroCategoria = Producto.objects.get(idCategoria = vCategoria)
    Producto.objects.create(idProducto = vId, nombreProducto = vNombre, descripcion = vDescripcion, marca = vMarca, stock = vStock, precio = vPrecio, fotoProducto = vFoto, categoria = vRegistroCategoria)

    
    return redirect('anadirp')
