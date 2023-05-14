from django.shortcuts import render

# Create your views here.
def principal (request):
    return render(request,'menu/principal.html')


def detergentes(request):
    return render(request,'menu/detergentes.html')

def productos(request):
    return render(request, 'menu/productos.html')