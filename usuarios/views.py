from django.shortcuts import render, redirect
from .forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
import logging
from django.contrib import auth, messages


def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form['nome_login'].value()
            senha = form['senha'].value()
            
        usuario = auth.authenticate(
            username = nome,
            password = senha
        )
        if usuario is not None:
            auth.login(request,usuario)
            messages.success(request,'Login realizado com sucesso!')
            return redirect('home')
        else:
            messages.error(request,'Não foi possível realizar o login! Tente novamente mais tarde')
            return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):

    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        
        if form.is_valid():
            if form['senha'].value() != form['senha1'].value():
                messages.error(request,'As senhas não coincidem')
                return redirect('cadastro')
                
            
            nome = form['nome_cadastro'].value()
            senha = form['senha'].value()
            email = form ['email'].value()

            print(nome,senha,email)
            
            if User.objects.filter(username=nome).exists():
                return redirect('cadastro')
            messages.error(request,'O usuário já existe')
            
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha

            )
            usuario.save()
            messages.success(request,'O usuário foi criado com sucesso')
            return redirect('login')


        


    return render(request, 'usuarios/cadastro.html', {'form':form})

def logout(request):
    messages.warning(request,'Logout realizado com sucesso')
    auth.logout(request)
    return redirect('home')