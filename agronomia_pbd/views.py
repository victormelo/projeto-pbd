#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from models import Usuario
from django.http import HttpResponse, HttpResponseRedirect

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
    return render_to_response('logado.html', {'usuario' : m})
