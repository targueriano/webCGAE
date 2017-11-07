# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Relatorio, Services, Comunicados, Escala_Limpeza, Vistoria,\
Escala_Servidores, Limpeza, Prontuario, Prontuario_detalhe, Educacional, Educacional_detalhe
# Register your models here.


class RelatorioAdmin(admin.ModelAdmin):
    model = Relatorio
    list_display = ['denunciante','denunciado', 'titulo', 'texto', 'artigo', 'medida_prevista',
                    'data', 'servidor', 'denuncia',
                    'comunicado_discente','encaminhado_conciliacao', 'protocolado',
                    'medida_aplicada', 'tipo_medida']

    list_filter = [ 'denunciante', 'servidor' , 'medida_prevista', 'data', 'medida_aplicada',
                    'denuncia', 'comunicado_discente',
                    'encaminhado_conciliacao', 'protocolado',
                    'tipo_medida']
    search_fields = ['denunciado__nome', 'denunciante']

    save_on_top = True

class VistoriaAdmin(admin.ModelAdmin):
    model = Vistoria
    list_display = ['quarto', 'portas', 'armarios', 'vidros','beliches',
                    'mesa', 'detalhes', 'motivo', 'data']
    list_filter = ['data', 'quarto', 'motivo']
    search_fields = ['quarto',]
    save_on_top = True

class LimpezaAdmin(admin.ModelAdmin):
    model = Limpeza
    list_display = ['quarto', 'semana_inicio', 'semana_fim',
                    'limpeza', 'lixo', 'verificado', 'detalhes', 'servidor']
    list_filter = ['quarto', 'semana_inicio', 'servidor']
    save_on_top = True
    actions_on_top = True

class ComunicadosAdmin(admin.ModelAdmin):
    model = Comunicados
    list_display = ['tipo', 'aluno', 'texto', 'data', 'servidor']
    list_filter = ['tipo', 'aluno', 'data', 'servidor']
    search_fields = ['aluno__nome']
    save_on_top = True

class ServicesAdmin(admin.ModelAdmin):
    model = Services
    list_display = ['local', 'atividade', 'data_inicial',
                    'servidor', 'finalizado',
                    'data_final', 'motivo']
    list_filter = ['local', 'finalizado', 'data_inicial']
    save_on_top = True
    actions_on_top = False

class Educacional_detalheAdmin(admin.TabularInline):
    model = Educacional_detalhe
    list_display = ['educacional','ocorrencia', 'setor', 'servidor', 'data']
    extra = 0

class EducacionalAdmin(admin.ModelAdmin):
    model = Educacional
    list_display = ['aluno',]
    save_on_top = True
    actions_on_top = True
    search_fields = ['aluno__nome']
    inlines = [Educacional_detalheAdmin]

class Prontuario_detalheAdmin(admin.TabularInline):
    model = Prontuario_detalhe
    list_display = ['prontuario', 'evento', 'servidor', 'data']
    extra = 0

class ProntuarioAdmin(admin.ModelAdmin):
    model = Prontuario
    list_display = ['aluno',]
    list_filter = ['aluno',]
    save_on_top = True
    actions_on_top = True
    search_fields = ['aluno__nome']
    inlines = [Prontuario_detalheAdmin]

class Escala_LimpezaAdmin(admin.ModelAdmin):
    model = Escala_Limpeza
    list_display = ['semana_inicio', 'semana_fim', 'lixo', 'limpeza', 'quarto',
    'nota']
    list_filter = ['semana_inicio', 'quarto', 'nota']
    save_on_top = True
    actions_on_top = True

class Escala_ServidoresAdmin(admin.ModelAdmin):
    model = Escala_Servidores
    list_display = ['dia_da_semana', 'horario_de_inicio', 'intervalo_inicio',
                    'intervalo_fim', 'horario_de_saida', 'servidor']

    list_filter = ['dia_da_semana', 'servidor']
    save_on_top = True
    actions_on_top = True

admin.site.register(Limpeza, admin_class=LimpezaAdmin)
admin.site.register(Services, admin_class=ServicesAdmin)
admin.site.register(Comunicados, admin_class=ComunicadosAdmin)
admin.site.register(Prontuario, admin_class=ProntuarioAdmin)
admin.site.register(Educacional, admin_class=EducacionalAdmin)
admin.site.register(Escala_Limpeza, admin_class=Escala_LimpezaAdmin)
admin.site.register(Escala_Servidores, admin_class=Escala_ServidoresAdmin)
admin.site.register(Relatorio, admin_class=RelatorioAdmin)
admin.site.register(Vistoria, admin_class=VistoriaAdmin)
