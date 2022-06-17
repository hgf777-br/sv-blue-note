from datetime import date
from django.db import models

from boat.cadastro.models import Fornecedor, Servico, Setor

class Evento(models.Model):
    date = models.DateField(default=date.today)
    descricao = models.TextField()
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    realizado = models.BooleanField()
    setor = models.ForeignKey(Setor, on_delete=models.DO_NOTHING)
    servico = models.ForeignKey(Servico, on_delete=models.DO_NOTHING)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.servico.name
