from calendar import month
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from boat.cadastro.models import Fornecedor, Servico, Setor
from django.utils.html import escape
from boat.cadastro.forms import ServicoForm


@login_required
def setor(request):
    setores = Setor.objects.all()
    return render(request, 'cadastro/setor.html', {
        'titulo': 'Setor',
        'setores': setores
    })

@login_required
def setor_insert(request):
    if request.method == 'POST':
        setores = Setor.objects.all()
        names = [setor.name for setor in setores]
        name = escape(request.POST['name'])
        if name in names:
            messages.error(request, 'Este setor já existe')
            return redirect('cadastro:setor_insert')
        else:
            setor = Setor(name=name)
            setor.save()
            return redirect('cadastro:setor')
    else:
        return render(request, 'cadastro/setor_insert.html', {
            'titulo': 'Setor'
        })

@login_required
def setor_edit(request, setor_id):
    if request.method == 'POST':
        setores = Setor.objects.all()
        names = [setor.name for setor in setores]
        name = escape(request.POST['name'])
        if name in names:
            messages.error(request, 'Este setor já existe')
            setor_edit = Setor.objects.get(id=setor_id)
            return render(request, 'cadastro/setor_edit.html', {
                'titulo': 'Setor',
                'setor_edit': setor_edit,
            })
        else:
            setor_edit = Setor.objects.get(id=setor_id)
            setor_edit.name = name
            setor_edit.save()
            messages.success(request, f'Setor { setor_edit.name } alterado no sistema')
            return redirect('cadastro:setor')
            
    setor_edit = Setor.objects.get(id=setor_id)
    return render(request, 'cadastro/setor_edit.html', {
        'titulo': 'Setor',
        'setor_edit': setor_edit,
    })

@login_required
def setor_delete(request, setor_id):
    if request.method == 'POST':
        setor_del = Setor.objects.get(id=setor_id)
        setor_del.delete()
        messages.success(request, f'Setor { setor_del.name } foi excluído do sistema')
        return redirect('cadastro:setor')
            
    setor_del = Setor.objects.get(id=setor_id)
    return render(request, 'cadastro/setor_delete.html', {
        'titulo': 'Setor',
        'setor_del': setor_del,
    })

@login_required
def servico(request):
    servicos = Servico.objects.all().select_related('setor')
    return render(request, 'cadastro/servico.html', {
        'titulo': 'Serviço',
        'servicos': servicos
    })

@login_required
def servico_insert(request):
    servico = Servico()
    if request.method == 'POST':
        servicos = Servico.objects.all()
        names = [servico.name for servico in servicos]
        name = escape(request.POST['name'])
        setor = Setor.objects.get(id=request.POST['setor'])
        period = servico.get_choice(request.POST['period'])
        # next_service = escape(request.POST['next_service'])
        # today = date.today()
        # if next_service == '':
        #     next_service = today + relativedelta(months=PERIODS[service_period])
        # else:
        #     next_service = date.fromisoformat(request.POST['next_service'])
        if name in names:
            messages.error(request, 'Este serviço já existe')
            return redirect('cadastro:servico_insert')
        # elif next_service < today:
        #     messages.error(request, 'A próxima data deve ser posterior a hoje')
        #     return redirect('cadastro:servico_insert')
        else:
            servico = Servico(name=name, period=period, setor=setor)
            servico.save()
            next_page = request.GET.get('next_page')
            return redirect(next_page)
    else:
        setores = Setor.objects.all()
        next_page = request.GET.get('next_page')
        return render(request, 'cadastro/servico_insert.html', {
            'titulo': 'Serviço',
            'next_page': next_page,
            'servico': servico,
            'setores': setores,
        })
        
@login_required
def servico_edit(request, servico_id):
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
    if request.method == 'POST':
        servico_edit = Servico.objects.get(id=servico_id)
        servicos = Servico.objects.all()
        names = [servico.name for servico in servicos]
        name = escape(request.POST['name'])
        setor = Setor.objects.get(id=request.POST['setor'])
        service_period = request.POST['service_period']
        next_service = escape(request.POST['next_service'])
        today = date.today()
        if next_service == '':
            next_service = today + relativedelta(months=PERIODS[service_period])
        else:
            next_service = date.fromisoformat(request.POST['next_service'])
        if name != servico_edit.name and name in names:
            messages.error(request, 'Este serviço já existe')
            setores = Setor.objects.all()
            return render(request, 'cadastro/servico_edit.html', {
                'titulo': 'Serviço',
                'servico_edit': servico_edit,
                'setores': setores,
                'periods': PERIODS,
            })
        elif next_service < today:
            messages.error(request, 'A próxima data deve ser posterior a hoje')
            setores = Setor.objects.all()
            return render(request, 'cadastro/servico_edit.html', {
                'titulo': 'Serviço',
                'servico_edit': servico_edit,
                'setores': setores,
                'periods': PERIODS,
            })
        else:
            setor_edit = Servico.objects.get(id=servico_id)
            setor_edit.name = name
            setor_edit.service_period = service_period
            setor_edit.next_service = next_service
            setor_edit.setor = setor
            setor_edit.save()
            messages.success(request, f'Serviço { setor_edit.name } alterado no sistema')
            return redirect('cadastro:servico')
            
    servico_edit = Servico.objects.get(id=servico_id)
    setores = Setor.objects.all()
    return render(request, 'cadastro/servico_edit.html', {
        'titulo': 'Serviço',
        'servico_edit': servico_edit,
        'setores': setores,
        'periods': PERIODS,
    })

@login_required
def servico_delete(request, servico_id):
    if request.method == 'POST':
        servico_del = Servico.objects.get(id=servico_id)
        servico_del.delete()
        messages.success(request, f'Serviço { servico_del.name } foi excluído do sistema')
        return redirect('cadastro:servico')
            
    servico_del = Servico.objects.get(id=servico_id)
    return render(request, 'cadastro/servico_delete.html', {
        'titulo': 'Serviço',
        'servico_del': servico_del,
    })
    
@login_required
def fornecedor(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'cadastro/fornecedor.html', {
        'titulo': 'Fornecedor',
        'fornecedores': fornecedores
    })

@login_required
def fornecedor_insert(request):
    if request.method == 'POST':
        servicos = Servico.objects.all()
        names = [servico.name for servico in servicos]
        name = escape(request.POST['name'])
        setor = Setor.objects.get(id=request.POST['setor'])
        service_period = request.POST['service_period']
        next_service = escape(request.POST['next_service'])
        today = date.today()
        if next_service == '':
            next_service = today + relativedelta(months=PERIODS[service_period])
        else:
            next_service = date.fromisoformat(request.POST['next_service'])
        if name in names:
            messages.error(request, 'Este serviço já existe')
            return redirect('cadastro:servico_insert')
        elif next_service < today:
            messages.error(request, 'A próxima data deve ser posterior a hoje')
            return redirect('cadastro:servico_insert')
        else:
            servico = Servico(name=name, service_period=service_period, next_service=next_service, setor=setor)
            servico.save()
            return redirect('cadastro:servico')
    else:
        setores = Setor.objects.all()
        return render(request, 'cadastro/servico_insert.html', {
            'titulo': 'Serviço',
            'setores': setores,
            'periods': PERIODS,
        })
        
@login_required
def fornecedor_edit(request, servico_id):
    if request.method == 'POST':
        servico_edit = Servico.objects.get(id=servico_id)
        servicos = Servico.objects.all()
        names = [servico.name for servico in servicos]
        name = escape(request.POST['name'])
        setor = Setor.objects.get(id=request.POST['setor'])
        service_period = request.POST['service_period']
        next_service = escape(request.POST['next_service'])
        today = date.today()
        if next_service == '':
            next_service = today + relativedelta(months=PERIODS[service_period])
        else:
            next_service = date.fromisoformat(request.POST['next_service'])
        if name != servico_edit.name and name in names:
            messages.error(request, 'Este serviço já existe')
            setores = Setor.objects.all()
            return render(request, 'cadastro/servico_edit.html', {
                'titulo': 'Serviço',
                'servico_edit': servico_edit,
                'setores': setores,
                'periods': PERIODS,
            })
        elif next_service < today:
            messages.error(request, 'A próxima data deve ser posterior a hoje')
            setores = Setor.objects.all()
            return render(request, 'cadastro/servico_edit.html', {
                'titulo': 'Serviço',
                'servico_edit': servico_edit,
                'setores': setores,
                'periods': PERIODS,
            })
        else:
            setor_edit = Servico.objects.get(id=servico_id)
            setor_edit.name = name
            setor_edit.service_period = service_period
            setor_edit.next_service = next_service
            setor_edit.setor = setor
            setor_edit.save()
            messages.success(request, f'Serviço { setor_edit.name } alterado no sistema')
            return redirect('cadastro:servico')
            
    servico_edit = Servico.objects.get(id=servico_id)
    setores = Setor.objects.all()
    return render(request, 'cadastro/servico_edit.html', {
        'titulo': 'Serviço',
        'servico_edit': servico_edit,
        'setores': setores,
        'periods': PERIODS,
    })

@login_required
def fornecedor_delete(request, servico_id):
    if request.method == 'POST':
        servico_del = Servico.objects.get(id=servico_id)
        servico_del.delete()
        messages.success(request, f'Serviço { servico_del.name } foi excluído do sistema')
        return redirect('cadastro:servico')
            
    servico_del = Servico.objects.get(id=servico_id)
    return render(request, 'cadastro/servico_delete.html', {
        'titulo': 'Serviço',
        'servico_del': servico_del,
    })
    