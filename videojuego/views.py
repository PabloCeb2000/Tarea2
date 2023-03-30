from django.shortcuts import render
from rest_framework import viewsets
from .models import Usuarios, Partidas
from . serializers import UsauriosSerializer,PartidasSerializer
from django.http import HttpResponse
from json import loads,dumps
from django.views.decorators.csrf import csrf_exempt
from json import loads, dumps
import sqlite3
import requests

def index(request):
    return render(request, 'index.html')


class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsauriosSerializer
    
class PartidasViewSet(viewsets.ModelViewSet):
    queryset = Partidas.objects.all() 
    
    serializer_class = PartidasSerializer