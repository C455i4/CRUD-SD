from django.db import models
from django.conf import settings
# Create your models here.

class Acao(models.Model):  
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, null=False)
    codigo_acao = models.CharField(max_length=10, blank=False, null=False)  
    descricao = models.TextField(max_length=200)
    data = models.DateField()
    open = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=False)
    close = models.DecimalField(max_digits=6, decimal_places=2,blank=False, null=False)
    high = models.DecimalField(max_digits=6, decimal_places=2,blank=False, null=False)
    low = models.DecimalField(max_digits=6, decimal_places=2,blank=False, null=False)
    volume = models.IntegerField(blank=False, null=False, default=0)