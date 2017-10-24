# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Dificuldade_por_disciplina, Rendimento

# Register your models here.
class Dificuldade_por_disciplinaAdmin(admin.ModelAdmin):
    model=Dificuldade_por_disciplina
    list_display = ['disciplina', 'numero_de_alunos']
    list_filter = ['disciplina']
    search_fields = ['disciplina']
    save_on_top = True

class RendimentoAdmin(admin.ModelAdmin):
    model=Rendimento
    list_display = ['ano', 'aprovados_sem_exame', 'aprovados_com_exame',
                    'com_dependencia', 'reprovados' ]
    list_filter = ['ano' ]
    save_on_top = True

admin.site.register(Dificuldade_por_disciplina,Dificuldade_por_disciplinaAdmin)
admin.site.register(Rendimento, RendimentoAdmin)
