from rest_framework import serializers
#from dataclasses import fields
from . models import Usuarios, Partidas

class UsauriosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'

class PartidasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partidas
        fields = '__all__'