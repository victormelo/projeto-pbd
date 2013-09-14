#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Usuario
from django.http import HttpResponse, HttpResponseRedirect
from forms import UsuarioForm, ExperimentoForm

def register(request):
    cadastro = 0
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try:
                Usuario(senha = cd['senha'], email = cd['email'], nome = cd['nome'], sobrenome=cd['sobrenome'],
                    instituicao=cd['instituicao'], observacao = cd['observacao'], cidade=cd['cidade'],
                    pais=cd['pais'], estado=cd['estado'], endereco = cd['endereco']).save()
                return HttpResponseRedirect('/logado/')

            except:
                cadastro= 1
        else:
            cadastro = 1
    else:
        form = UsuarioForm()
    return render_to_response('index.html', {'form' : form, 'cadastro' : cadastro})

def index(request):
    form = UsuarioForm()
    return render_to_response('index.html', {'form' : form})

def registrarExperimento(request):
    try:
        m = Usuario.objects.get(id=request.session['member_id'])
    except:
        return HttpResponseRedirect("/")
        m = None
    
    if request.method == 'POST':
        form = ExperimentoForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/erro/')
    else:
        form = ExperimentoForm()
    return render_to_response('registrarExperimento.html', {'form' : form, 'usuario' : m})

def login(request):
    try:
        m = Usuario.objects.get(email=request.POST['email'])
    except:
        m = None
        
    if (m):
        if m.senha == request.POST['senha']:
            request.session['member_id'] = m.id
            return HttpResponseRedirect("/logado/")
        else:
            return HttpResponseRedirect("/")
    else:
         return HttpResponseRedirect("/")
                   
def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

def logado(request):
    try:
        m = Usuario.objects.get(id=request.session['member_id'])
    except:
        return HttpResponseRedirect("/")
        m = None
    return render_to_response('logado.html', {'usuario' : m})
