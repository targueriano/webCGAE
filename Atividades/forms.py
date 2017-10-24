from django import forms
from .models import (Comunicados, Relatorio, Prontuario, Prontuario_detalhe,
                                            Educacional, Educacional_detalhe)
from django.forms import inlineformset_factory
from django.contrib.admin import widgets
#from tinymce.widgets import TinyMCE


class ComunicadoForm(forms.ModelForm):
    #texto = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 10}))
    class Meta:
        model = Comunicados
        fields = ('tipo', 'aluno', 'texto', 'servidor')
        exclude = ('data',)

class RelatorioForm(forms.ModelForm):
    #texto = forms.CharField(widget=TinyMCE(attrs={'cols': 100, 'rows': 10}))
    #titulo = forms.CharField(widget=TinyMCE(attrs={'cols': 50, 'rows': 1}))

    class Meta:
        model = Relatorio
        fields = '__all__'
        exclude = ('data','controle','denuncia', 'protocolado',
                   'comunicado_discente', 'medida_aplicada','tipo_medida',
                   'avaliado', 'encaminhado_conciliacao')

class ProntuarioDetalheForm(forms.ModelForm):

    class Meta:
        model = Prontuario_detalhe
        fields = '__all__'
        exclude = ['data',]

class ProntuarioForm(forms.ModelForm):
    class Meta:
        model = Prontuario
        fields = '__all__'


class EducacionalForm(forms.ModelForm):
    class Meta:
        model = Educacional
        fields = '__all__'

class EducacionalDetalheForm(forms.ModelForm):
    class Meta:
        model = Educacional_detalhe
        fields = '__all__'
        exclude = ['data',]


Prontuario_detalhe_formset = inlineformset_factory(Prontuario, Prontuario_detalhe,
                                                form=ProntuarioDetalheForm,
                                                extra=1)

Educacional_detalhe_formset = inlineformset_factory(Educacional, Educacional_detalhe,
                                                    form=EducacionalDetalheForm,
                                                    extra=1)
