from django.contrib import admin
from boat.cadastro.models import Servico, Setor, Fornecedor

@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('name', 'setor', 'service_period', 'next_service')
    search_fields = ('name',)
    
@admin.register(Fornecedor)
class ForncedorAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'email', 'phone')
    search_fields = ('name', 'contact')