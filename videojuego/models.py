from django.db import models

# Create your models here.
class Usuarios(models.Model):
    password = models.CharField(max_length=30)



class Partidas(models.Model):
    fecha = models.CharField(max_length=10)
    usuarios = models.ForeignKey(Usuarios, related_name= 'id_usuario', on_delete=models.CASCADE)
    minutos_jugados = models.IntegerField()
    puntaje = models.IntegerField()



