from datetime import date
from django.db import models

class Setor(models.Model):
    name = models.CharField(max_length=16)


class Servico(models.Model):
    name = models.CharField(max_length=32)
    period = models.CharField(max_length=16)
    next = models.DateField(default=date.today)
    setor = models.ForeignKey(Setor, on_delete=models.DO_NOTHING)
    
class Fornecedor(models.Model):
    name = models.CharField(max_length=32)
    contact = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    servico = models.ForeignKey(Servico, on_delete=models.DO_NOTHING)