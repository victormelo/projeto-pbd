from django.db import models

class Usuario(models.Model):
    senha = models.CharField(max_length = 80)
    email = models.CharField(max_length = 80, unique = True)
    nome = models.CharField(max_length = 80)
    sobrenome = models.CharField(max_length = 80)
    instituicao = models.CharField(max_length = 80)
    observacao = models.CharField(max_length = 80)
    pais = models.CharField(max_length=80)
    cidade = models.CharField(max_length = 80)
    endereco = models.CharField(max_length = 80)
    estado = models.CharField(max_length = 80)

class CondicaoSolo(models.Model):
    nome = models.CharField(max_length = 80)
    descricao = models.CharField(max_length = 80) 

class Solo(models.Model):
    nome = models.CharField(max_length = 80)
    diametro = models.FloatField()
    frequencia = models.FloatField()
    argila = models.FloatField()
    silte = models.FloatField()
    areia = models.FloatField()
    tempo = models.FloatField()
    lamina = models.FloatField()
    densidadeSolo = models.FloatField()
    densidadeDaParticula = models.FloatField()
    teorUmidade = models.FloatField()
    teorUmidadeFinal = models.FloatField()
    resistenciaDoSolo = models.FloatField()
    condicao = models.ForeignKey(CondicaoSolo)

class Teste(models.Model):
    usuario = models.ForeignKey(Usuario)
    identificacao = models.CharField(max_length = 80)
    solos = models.ManyToManyField(Solo)

class Localizacao(models.Model):
    solo = models.ForeignKey(Solo)
    latitude = models.FloatField()
    longitude = models.FloatField()
    altitude = models.FloatField()
    municipio = models.CharField(max_length=80)
    estado = models.CharField(max_length=80)
    pais = models.CharField(max_length=80)
    

    
