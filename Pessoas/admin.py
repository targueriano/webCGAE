# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import  Aluno, Perfil_do_Servidor, Familia, Perfil_do_Aluno, Curso, Turma

# Register your models here.
class AlunoAdmin(admin.ModelAdmin):
    model=Aluno
    list_display = ['matricula', 'nome', 'nascimento', 'cidade',
                    'turma','telefone', 'alojamento',
                    'emancipado', 'transferido', 'abandonou','faleceu']
    list_filter = ['alojamento', 'turma', 'cidade', 'transferido', 'abandonou', 'emancipado', 'faleceu']
    search_fields = ['matricula', 'nome']
    save_on_top = True

class ServidorAdmin(admin.ModelAdmin):
    model=Perfil_do_Servidor
    list_display = ['matricula', 'servidor', 'carreira','cargo']
    list_filter = ['cargo']
    search_fields = ['servidor__username']
    save_on_top = True

class FamiliaAdmin(admin.ModelAdmin):
    model=Familia
    list_display = ['aluno','pai', 'profissao_pai', 'mae', 'profissao_mae',
                    'responsavel','telefone', 'telefone2', 'telefone3']
    search_fields = ['aluno__nome']
    save_on_top = True


class PerfilAdmin(admin.ModelAdmin):
    model = Perfil_do_Aluno
    list_display = ['aluno', 'nota_ensino', 'nota_comportamento', 'saude', 'reside', 'objetivos',
                    'foto', 'motivo', 'curso', 'forma']
    list_filter = ['reside', 'motivo', 'objetivos']
    search_fields = ['aluno__nome']
    save_on_top = True


class CursoAdmin(admin.ModelAdmin):
    model = Curso
    list_display = ['curso',]
    list_filter = ['curso',]
    save_on_top = True

class TurmaAdmin(admin.ModelAdmin):
    model = Turma
    list_display = ['curso', 'turma']
    list_filter = ['curso', 'turma']

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Perfil_do_Servidor, ServidorAdmin)

admin.site.register(Familia, FamiliaAdmin)
admin.site.register(Perfil_do_Aluno, PerfilAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Turma, TurmaAdmin)
