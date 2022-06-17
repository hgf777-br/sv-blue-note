from datetime import date
from django.db import models

class Setor(models.Model):
    name = models.CharField(max_length=16)
    
    def __str__(self):
        return self.name
    
class Servico(models.Model):
    name = models.CharField(max_length=32)
    service_period = models.CharField(max_length=16)
    next_service = models.DateField(default=date.today, blank=True)
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    
class Fornecedor(models.Model):
    name = models.CharField(max_length=32)
    contact = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    # servico = models.ManyToManyField(Servico)
    
    def __str__(self):
        return self.name