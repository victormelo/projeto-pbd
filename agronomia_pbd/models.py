from django.db import models

# Create your models here.
#testando push

class Usuario(models.Model):
    nome = models.CharField(max_length = 80)
    email = models.CharField(max_length = 80)
    login = models.CharField(max_length = 10)
    senha = models.CharField(max_length = 80)
    instituicao = models.CharField(max_length = 80)
    observacao = models.CharField(max_length = 80)
    cidade = models.CharField(max_length = 80)
    fazenda = models.CharField(max_lenght = 80)
    estado = models.CharField(max_lenght = 80)
    rua = models.CharField(max_lenght = 80)
    
class Experimento(models.Model):
    usuario = models.ForeignKey(Usuario)
    nome = models.CharField(max_lenght = 80)

class Experimento_Instrumentos(models.Model):
    instrumentos = models.ForeignKey(Instrumento)
    experimento = models.ForeignKey(Experimento)

class Instrumento(models.Model):
    nome = models.CharField(max_lenght = 80)
    tipo = models.CharField(max_lenght = 80)
    
class Localizacao(models.Model):
    experimento = models.ForeignKey(Experimento)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    
class Tratamento(models.Model):
    experimento = models.ForeignKey(Experimento)
    nome = models.CharField(max_lenght = 80)
    descricao = models.CharField(max_lenght = 80)
    
class Experimento_Solo(models.Model):
    experimento = models.ForeignKey(Experimento)
    solo = models.ForeignKey(Solo)
    
class Solo(models.Model):
    nome = models.CharField(max_lenght = 80)
    diametro = models.FloatField()
    frequencia = models.FloatField()
    argila = models.FloatField()
    silte = models.FloatField()
    areia = models.FloatField()
    tempo = models.FloatField()
    lamina = models.FloatField()
    densidade = models.FloatField()
    teorUmidade = models.FloatField()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    