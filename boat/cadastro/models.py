from datetime import date
import string
from django.db import models

class Setor(models.Model):
    name = models.CharField(max_length=16)
    
    def __str__(self):
        return self.name
    
# class Servico(models.Model):
#     name = models.CharField(max_length=32)
#     service_period = models.CharField(max_length=16)
#     next_service = models.DateField(default=date.today, blank=True)
#     setor = models.ForeignKey(Setor, on_delete=models.PROTECT)
    
#     def __str__(self):
#         return self.name

class Servico(models.Model):
    PERIODS = [
        (0, 'pontual'),
        (3, 'trimestral'),
        (6, 'semestral'),
        (12, 'anual'),
        (24, 'a cada 2 anos'),
        (36, 'a cada 3 anos'),
        (60, 'a cada 5 anos'),
        (120, 'a cada 10 anos'),
    ]
    name = models.CharField(max_length=32)
    period = models.PositiveSmallIntegerField(
        choices = PERIODS,
        default = 0,
    )
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
    
    def display_choices(self):
        return [period[1] for period in self.PERIODS]
    
    def get_choice(self, choice: str):
        # return [x[0] for x in self.PERIODS if x[1] == choice][0]
        return next(x[0] for x in self.PERIODS if x[1] == choice)
    
class Fornecedor(models.Model):
    name = models.CharField(max_length=32)
    contact = models.CharField(max_length=64)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    # servico = models.ManyToManyField(Servico)
    
    def __str__(self):
        return self.name