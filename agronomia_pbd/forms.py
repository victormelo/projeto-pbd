#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

class DefaultForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DefaultForm, self).__init__(*args, **kwargs)
        for k, field in self.fields.items():
            if 'required' in field.error_messages:
                field.error_messages['required'] = u'É necesssário preencher o campo abaixo.'
            if 'invalid' in field.error_messages:
                field.error_messages['invalid'] = u"Entre um valor válido."
            field.widget.attrs["class"] = 'form-control'
            
class UsuarioForm(DefaultForm):
    ESTADOS_CHOICES = (
        ('ac', 'Acre'), 
        ('al', 'Alagoas'), 
        ('am', 'Amazonas'), 
        ('ap', 'Amapá'), 
        ('ba', 'Bahia'), 
        ('ce', 'Ceará'), 
        ('df', 'Distrito Federal'), 
        ('es', 'Espírito Santo'), 
        ('go', 'Goiás'), 
        ('ma', 'Maranhão'), 
        ('mt', 'Mato Grosso'), 
        ('ms', 'Mato Grosso do Sul'), 
        ('mg', 'Minas Gerais'), 
        ('pa', 'Pará'), 
        ('pb', 'Paraíba'), 
        ('pr', 'Paraná'), 
        ('pe', 'Pernambuco'), 
        ('pi', 'Piauí'), 
        ('rj', 'Rio de Janeiro'), 
        ('rn', 'Rio Grande do Norte'), 
        ('ro', 'Rondônia'), 
        ('rs', 'Rio Grande do Sul'), 
        ('rr', 'Roraima'), 
        ('sc', 'Santa Catarina'), 
        ('se', 'Sergipe'), 
        ('sp', 'São Paulo'), 
        ('to', 'Tocantins'), 
    )
    nome = forms.CharField(max_length = 80)
    sobrenome = forms.CharField(max_length = 80)
    email = forms.EmailField(max_length = 80)
    senha = forms.CharField(max_length = 80, widget=forms.PasswordInput())
    repitaSenha = forms.CharField(max_length = 80, widget=forms.PasswordInput(), label=u"Repita a Senha")
    instituicao = forms.CharField(max_length = 80, label=u"Instituição")
    cidade = forms.CharField(max_length = 80)
    endereco = forms.CharField(max_length = 80, required=False, label=u"Endereço (rua, numero)")
    estado = forms.ChoiceField(choices=ESTADOS_CHOICES)
    observacao = forms.CharField(widget = forms.Textarea, label=u"Observações", required=False)

class ExperimentoForm(DefaultForm):
    nomeExperimento = forms.CharField(max_length = 80, label=u"Nome do Experimento")
    latitude = forms.FloatField()
    longitude = forms.FloatField()
    altitude = forms.FloatField()
    nomeSolo = forms.CharField(max_length = 80, label=u"Nome do Solo")
    nomeTratamento = forms.CharField(max_length=80, label=u"Nome do Tratamento")
    descricaoTratamento = forms.CharField(max_length=80, label=u"Descrição do Tratamento")
    #curva de infiltração
    tempo = forms.FloatField()
    lamina = forms.FloatField()
    
    #curva de granulometria
    diametro = forms.FloatField(label=u"Diâmetro")
    frequencia = forms.FloatField(label=u"Frequência")
    
    silte = forms.FloatField()
    areia = forms.FloatField()
    argila = forms.FloatField()
    
    densidadeSolo = forms.FloatField(label=u"Densidade do solo (g.cm ^ -3)")
    densidadeParticula = forms.FloatField(label=u"Densidade da particula (g.cm ^ -3)")
    resistenciaSolo = forms.FloatField(label=u"Resistência do solo à penetração (MPa)")
    
    