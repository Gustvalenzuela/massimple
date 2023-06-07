from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import usuarioSerializer
from menu.models import Usuario


# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
def lista_usuario(request):
    if request.method == 'GET':
        usuario = Usuario.objects.all()
        serializer = usuarioSerializer(usuario, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = usuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


