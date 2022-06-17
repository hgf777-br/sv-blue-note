from django.contrib import admin
from boat.manutencao.models import Evento

@admin.register(Evento)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('date', 'setor', 'servico', 'fornecedor', 'valor', 'realizado', 'descricao')
    search_fields = ('setor', 'sevico', 'fornecedor')
