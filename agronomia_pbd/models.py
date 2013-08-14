from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length = 80)
    email = models.CharField(max_length = 80)
    senha = models.CharField(max_length = 80)
    instituicao = models.CharField(max_length = 80)
    observacao = models.CharField(max_length = 80)
    