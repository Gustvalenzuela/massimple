from django.shortcuts import render

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




