#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Usuario, Solo, CondicaoSolo
from django.http import HttpResponse, HttpResponseRedirect
from forms import UsuarioForm, TesteForm, SoloForm

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
        form_solo = SoloForm(request.POST)

        form = TesteForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/erro/')
    else:
        form_solo = SoloForm()
        form = TesteForm()
    return render_to_response('registrarTeste.html', {'form' : form, 'form_solo' : form_solo, 'usuario' : m})

def registrarSolo(request):
    try:
        m = Usuario.objects.get(id=request.session['member_id'])
    except:
        return HttpResponseRedirect("/")
        m = None
    
    cadastro = 0
    if request.method == 'POST':
        form = SoloForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # try:
            condicaoSolo = CondicaoSolo(nome = cd['nomeCondicao'], descricao = cd['descricaoCondicao'])
            condicaoSolo.save()
            Solo(condicao_id = condicaoSolo.id, nome = cd['nome'], diametro = cd['diametro'], frequencia = cd['frequencia'], 
                silte=cd['silte'], areia=cd['areia'], argila=cd['argila'],teorUmidade = cd['teorUmidade'],
                teorUmidadeFinal =cd['teorUmidadeFinal'],
                densidadeSolo=cd['densidadeSolo'], densidadeDaParticula=cd['densidadeDaParticula'], 
                resistenciaDoSolo = cd['resistenciaDoSolo'], tempo = cd['tempo'], lamina = cd['lamina']).save()
            return HttpResponseRedirect('/logado/register')
    # latitude=cd['latitude'], longitude = cd['longitude'], altitude=cd['altitude'],
    # resistenciaSolo = forms.FloatField(label=u"Resistência do solo à penetração (MPa)")
            # except:
                # cadastro = 1
        else:
            cadastro = 1
    else:
        form = UsuarioForm()
    return render_to_response('registrarTeste.html', {'form' : form, 'cadastro' : cadastro})
    

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
