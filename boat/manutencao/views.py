from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from boat.cadastro.models import Fornecedor, Servico, Setor
from boat.manutencao.models import Evento

@login_required
def realizado(request):
    eventos = Evento.objects.all()
    return render(request, 'manutencao/realizado.html', {
        'titulo': 'Manutenção',
        'eventos': eventos
    })

@login_required
def evento_insert(request):
    setores = Setor.objects.all()
    servicos = Servico.objects.all()
    fornecedores = Fornecedor.objects.all()
    return render(request, 'manutencao/evento_insert.html', {
        'titulo': 'Manutenção',
        'setores': setores,
        'servicos': servicos,
        'fornecedores': fornecedores,
    })

@login_required
def evento_edit(request):
    return render(request, 'manutencao/realizado.html', {})

@login_required
def evento_delete(request):
    return render(request, 'manutencao/realizado.html', {})
