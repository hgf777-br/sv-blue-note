from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib import messages
from boat.base.models import User
from django.utils.html import escape

def home(request):
    if request.user.is_authenticated:
        return redirect('manutencao:lista')
    else:    
        return redirect('base:login')

@login_required
def list_user(request):
    users = User.objects.all()
    return render(request, 'authenticate/list_user.html', {
        'users': users,
    })
    
def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('manutencao:lista')
        else:
            messages.success(request, 'Login incorreto. Tente de novo.')
            return redirect('base:login')
    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'Você saiu do sistema. Até logo!')
    return redirect('base:login')

@login_required
def register_user(request):
    if request.method == 'POST':
        first_name = escape(request.POST['first_name'])
        email = escape(request.POST['email'])
        password1 = escape(request.POST['password1'])
        password2 = escape(request.POST['password2'])
        if validate_user_email(email) and password1 == password2:
            user = User(first_name=first_name, email=email, password=password1)
            user.set_password(password1)
            user.save()
            return redirect('base:list_user')
        else:
            if not validate_user_email(email):
                messages.error(request, 'Entre com um email válido')
            if password1 != password2:
                messages.error(request, 'As duas senhas não conferem')
            return render(request, 'authenticate/register_user.html', {
                'first_name': first_name,
                'email': email,
                'password1': password1,
                'password2': password2,
            })

    return render(request, 'authenticate/register_user.html', {})
        
def validate_user_email( email ):
    try:
        validate_email( email )
        return True
    except ValidationError:
        return False

@login_required
def delete_user(request, user_id):
    if request.method == 'POST':
        user_del = User.objects.get(id=user_id)
        if request.user.id == user_id:    
            messages.error(request, 'Não é possível excluir o usuário logado no sistema')
            return redirect('base:list_user')
        else:
            user_del.delete()
            messages.success(request, f'Usuário { user_del.first_name } foi excluído do sistema')
            return redirect('base:list_user')
            
    user_del = User.objects.get(id=user_id)
    return render(request, 'authenticate/delete_user.html', {
        'user_del': user_del,
    })

@login_required
def edit_user(request, user_id):
    if request.method == 'POST':
        first_name = escape(request.POST['first_name'])
        email = escape(request.POST['email'])
        if validate_user_email(email):
            user_edit = User.objects.get(id=user_id)
            user_edit.first_name = first_name
            user_edit.email = email
            user_edit.save()
            return redirect('base:list_user')
        else:
            if not validate_user_email(email):
                messages.error(request, 'Entre com um email válido')
            return render(request, 'authenticate/register_user.html', {
                'first_name': first_name,
                'email': email,
            })
    
    user_edit = User.objects.get(id=user_id)
    return render(request, 'authenticate/edit_user.html', {
        'user_edit': user_edit,
    })