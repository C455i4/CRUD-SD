from django.db import models

class Acao(models.Model):  
    id = models.AutoField(primary_key=True, null=False)
    codigo_acao = models.CharField(max_length=10)  
    descricao = models.TextField(max_length=200)
    data = models.DateField()
    open = models.FloatField(blank=False)
    close = models.FloatField(blank=False)
    high = models.FloatField(blank=False)
    low = models.FloatField(blank=False)
    volume = models.IntegerField(blank=False)
