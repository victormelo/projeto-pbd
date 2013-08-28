#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from models import Usuario
from django.http import HttpResponse, HttpResponseRedirect

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/books/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {
        'form': form,
    })
    
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
        m = None
    return HttpResponse(u"Você está logado como: " + m.email)
    