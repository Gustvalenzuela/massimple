from rest_framework import serializers
from menu.models import Usuario

class usuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['idUsuario','rutUsuario','nombreUsuario', 'correoUsuario']