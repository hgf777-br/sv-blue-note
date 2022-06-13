from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from boat.cadastro.models import Setor
from django.utils.html import escape

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