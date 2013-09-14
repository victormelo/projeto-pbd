#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from models import Usuario

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
    
    PAIS_CHOICES = (
        ('África do Sul', 'África do Sul'),
        ('Albânia', 'Albânia'),
        ('Alemanha', 'Alemanha'),
        ('Andorra', 'Andorra'),
        ('Angola', 'Angola'),
        ('Anguilla', 'Anguilla'),
        ('Antigua', 'Antigua'),
        ('Arábia Saudita', 'Arábia Saudita'),
        ('Argentina', 'Argentina'),
        ('Armênia', 'Armênia'),
        ('Aruba', 'Aruba'),
        ('Austrália', 'Austrália'),
        ('Áustria', 'Áustria'),
        ('Azerbaijão', 'Azerbaijão'),
        ('Bahamas', 'Bahamas'),
        ('Bahrein', 'Bahrein'),
        ('Bangladesh', 'Bangladesh'),
        ('Barbados', 'Barbados'),
        ('Bélgica', 'Bélgica'),
        ('Benin', 'Benin'),
        ('Bermudas', 'Bermudas'),
        ('Botsuana', 'Botsuana'),
        ('Brasil', 'Brasil'),
        ('Brunei', 'Brunei'),
        ('Bulgária', 'Bulgária'),
        ('Burkina Fasso', 'Burkina Fasso'),
        ('botão', 'botão'),
        ('Cabo Verde', 'Cabo Verde'),
        ('Camarões', 'Camarões'),
        ('Camboja', 'Camboja'),
        ('Canadá', 'Canadá'),
        ('Cazaquistão', 'Cazaquistão'),
        ('Chade', 'Chade'),
        ('Chile', 'Chile'),
        ('China', 'China'),
        ('Cidade do Vaticano', 'Cidade do Vaticano'),
        ('Colômbia', 'Colômbia'),
        ('Congo', 'Congo'),
        ('Coréia do Sul', 'Coréia do Sul'),
        ('Costa do Marfim', 'Costa do Marfim'),
        ('Costa Rica', 'Costa Rica'),
        ('Croácia', 'Croácia'),
        ('Dinamarca', 'Dinamarca'),
        ('Djibuti', 'Djibuti'),
        ('Dominica', 'Dominica'),
        ('EUA', 'EUA'),
        ('Egito', 'Egito'),
        ('El Salvador', 'El Salvador'),
        ('Emirados Árabes', 'Emirados Árabes'),
        ('Equador', 'Equador'),
        ('Eritréia', 'Eritréia'),
        ('Escócia', 'Escócia'),
        ('Eslováquia', 'Eslováquia'),
        ('Eslovênia', 'Eslovênia'),
        ('Espanha', 'Espanha'),
        ('Estônia', 'Estônia'),
        ('Etiópia', 'Etiópia'),
        ('Fiji', 'Fiji'),
        ('Filipinas', 'Filipinas'),
        ('Finlândia', 'Finlândia'),
        ('França', 'França'),
        ('Gabão', 'Gabão'),
        ('Gâmbia', 'Gâmbia'),
        ('Gana', 'Gana'),
        ('Geórgia', 'Geórgia'),
        ('Gibraltar', 'Gibraltar'),
        ('Granada', 'Granada'),
        ('Grécia', 'Grécia'),
        ('Guadalupe', 'Guadalupe'),
        ('Guam', 'Guam'),
        ('Guatemala', 'Guatemala'),
        ('Guiana', 'Guiana'),
        ('Guiana Francesa', 'Guiana Francesa'),
        ('Guiné-bissau', 'Guiné-bissau'),
        ('Haiti', 'Haiti'),
        ('Holanda', 'Holanda'),
        ('Honduras', 'Honduras'),
        ('Hong Kong', 'Hong Kong'),
        ('Hungria', 'Hungria'),
        ('Iêmen', 'Iêmen'),
        ('Ilhas Cayman', 'Ilhas Cayman'),
        ('Ilhas Cook', 'Ilhas Cook'),
        ('Ilhas Curaçao', 'Ilhas Curaçao'),
        ('Ilhas Marshall', 'Ilhas Marshall'),
        ('Ilhas Turks & Caicos', 'Ilhas Turks & Caicos'),
        ('Ilhas Virgens (brit.),', 'Ilhas Virgens (brit.)'),
        ('Ilhas Virgens(amer.),', 'Ilhas Virgens(amer.)'),
        ('Ilhas Wallis e Futuna', 'Ilhas Wallis e Futuna'),
        ('Índia', 'Índia'),
        ('Indonésia', 'Indonésia'),
        ('Inglaterra', 'Inglaterra'),
        ('Irlanda', 'Irlanda'),
        ('Islândia', 'Islândia'),
        ('Israel', 'Israel'),
        ('Itália', 'Itália'),
        ('Jamaica', 'Jamaica'),
        ('Japão', 'Japão'),
        ('Jordânia', 'Jordânia'),
        ('Kuwait', 'Kuwait'),
        ('Latvia', 'Latvia'),
        ('Líbano', 'Líbano'),
        ('Liechtenstein', 'Liechtenstein'),
        ('Lituânia', 'Lituânia'),
        ('Luxemburgo', 'Luxemburgo'),
        ('Macau', 'Macau'),
        ('Macedônia', 'Macedônia'),
        ('Madagascar', 'Madagascar'),
        ('Malásia', 'Malásia'),
        ('Malaui', 'Malaui'),
        ('Mali', 'Mali'),
        ('Malta', 'Malta'),
        ('Marrocos', 'Marrocos'),
        ('Martinica', 'Martinica'),
        ('Mauritânia', 'Mauritânia'),
        ('Mauritius', 'Mauritius'),
        ('México', 'México'),
        ('Moldova', 'Moldova'),
        ('Mônaco', 'Mônaco'),
        ('Montserrat', 'Montserrat'),
        ('Nepal', 'Nepal'),
        ('Nicarágua', 'Nicarágua'),
        ('Niger', 'Niger'),
        ('Nigéria', 'Nigéria'),
        ('Noruega', 'Noruega'),
        ('Nova Caledônia', 'Nova Caledônia'),
        ('Nova Zelândia', 'Nova Zelândia'),
        ('Omã', 'Omã'),
        ('Palau', 'Palau'),
        ('Panamá', 'Panamá'),
        ('Papua-nova Guiné', 'Papua-nova Guiné'),
        ('Paquistão', 'Paquistão'),
        ('Peru', 'Peru'),
        ('Polinésia Francesa', 'Polinésia Francesa'),
        ('Polônia', 'Polônia'),
        ('Porto Rico', 'Porto Rico'),
        ('Portugal', 'Portugal'),
        ('Qatar', 'Qatar'),
        ('Quênia', 'Quênia'),
        ('Rep. Dominicana', 'Rep. Dominicana'),
        ('Rep. Tcheca', 'Rep. Tcheca'),
        ('Reunion', 'Reunion'),
        ('Romênia', 'Romênia'),
        ('Ruanda', 'Ruanda'),
        ('Rússia', 'Rússia'),
        ('Saipan', 'Saipan'),
        ('Samoa Americana', 'Samoa Americana'),
        ('Senegal', 'Senegal'),
        ('Serra Leone', 'Serra Leone'),
        ('Seychelles', 'Seychelles'),
        ('Singapura', 'Singapura'),
        ('Síria', 'Síria'),
        ('Sri Lanka', 'Sri Lanka'),
        ('St. Kitts & Nevis', 'St. Kitts & Nevis'),
        ('St. Lúcia', 'St. Lúcia'),
        ('St. Vincent', 'St. Vincent'),
        ('Sudão', 'Sudão'),
        ('Suécia', 'Suécia'),
        ('Suiça', 'Suiça'),
        ('Suriname', 'Suriname'),
        ('Tailândia', 'Tailândia'),
        ('Taiwan', 'Taiwan'),
        ('Tanzânia', 'Tanzânia'),
        ('Togo', 'Togo'),
        ('Trinidad & Tobago', 'Trinidad & Tobago'),
        ('Tunísia', 'Tunísia'),
        ('Turquia', 'Turquia'),
        ('Ucrânia', 'Ucrânia'),
        ('Uganda', 'Uganda'),
        ('Uruguai', 'Uruguai'),
        ('Venezuela', 'Venezuela'),
        ('Vietnã', 'Vietnã'),
        ('Zaire', 'Zaire'),
        ('Zâmbia', 'Zâmbia'),
        ('Zimbábue', 'Zimbábue'),
    )
    nome = forms.CharField(max_length = 80)
    sobrenome = forms.CharField(max_length = 80)
    email = forms.EmailField(max_length = 80)
    senha = forms.CharField(max_length = 80, widget=forms.PasswordInput())
    repitaSenha = forms.CharField(max_length = 80, widget=forms.PasswordInput(), label=u"Repita a Senha")
    instituicao = forms.CharField(max_length = 80, label=u"Instituição")
   
    pais = forms.ChoiceField(choices=PAIS_CHOICES, label=u"País", initial='Brasil') 
    estado = forms.ChoiceField(choices=ESTADOS_CHOICES, initial='pe')
    cidade = forms.CharField(max_length = 80)
    endereco = forms.CharField(max_length = 80, required=False, label=u"Endereço (rua, numero)")
    observacao = forms.CharField(widget = forms.Textarea, label=u"Observações", required=False)
    
    def clean(self):
        password1 = self.cleaned_data.get('senha')
        password2 = self.cleaned_data.get('repitaSenha')
        emailForm = self.cleaned_data.get('email')
        error = []
        try:
            usuarioExiste = Usuario.objects.get(email__exact = emailForm)
        except:
            usuarioExiste = None
        
        if(usuarioExiste):
            error.extend(['Email já cadastrado.'])
            
        
        if password1 and password1 != password2:
            error.extend(["As senhas não são iguais."])
        
        if error:
            raise forms.ValidationError(error)
        
        return self.cleaned_data

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
    
    