from django.db import models
from django.contrib.auth.models import User, UserManager


class Usuario(User):
    objects = UserManager()
    instituicao = models.CharField(max_length = 80)
    observacao = models.CharField(max_length = 80)
    cidade = models.CharField(max_length = 80)
    fazenda = models.CharField(max_length = 80)
    estado = models.CharField(max_length = 80)
    rua = models.CharField(max_length = 80)
class Solo(models.Model):
    nome = models.CharField(max_length = 80)
    diametro = models.FloatField()
    frequencia = models.FloatField()
    argila = models.FloatField()
    silte = models.FloatField()
    areia = models.FloatField()
    tempo = models.FloatField()
    lamina = models.FloatField()
    densidade = models.FloatField()
    teorUmidade = models.FloatField()
        
class Instrumento(models.Model):
    nome = models.CharField(max_length = 80)
    tipo = models.CharField(max_length = 80)
    
class Experimento(models.Model):
    usuario = models.ForeignKey(Usuario)
    nome = models.CharField(max_length = 80)
    instrumentos = models.ManyToManyField(Instrumento)
    solos = models.ManyToManyField(Solo)
    
class Localizacao(models.Model):
    experimento = models.ForeignKey(Experimento)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    
class Tratamento(models.Model):
    experimento = models.ForeignKey(Experimento)
    nome = models.CharField(max_length = 80)
    descricao = models.CharField(max_length = 80)
    
