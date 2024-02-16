from django.db import models

# Create your models here.

class Amostra(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    qntd_solucao = models.FloatField()()