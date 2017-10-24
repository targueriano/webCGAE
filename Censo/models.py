# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Dificuldade_por_disciplina(models.Model):
    disciplina = models.CharField(max_length=100, primary_key=True)
    numero_de_alunos = models.IntegerField(default=0,
            help_text='Quantidade de alunos com dificuldade nessa matéria.')

    def __str__(self):
        return self.disciplina

    def __unicode__(self):
        return self.disciplina

    class Meta:
        verbose_name = "Aluno com dificuldade na disciplina"
        verbose_name_plural = "Alunos com dificuldade por disciplina"

class Rendimento(models.Model):
    aprovados_sem_exame = models.IntegerField(default=0)
    aprovados_com_exame = models.IntegerField(default=0)
    reprovados = models.IntegerField(default=0)
    com_dependencia = models.IntegerField(default=0)
    ano = models.IntegerField(default=2016, help_text='Ano anterior ao vigente.')

    def __str__(self):
        return str(self.ano)

    def __unicode__(self):
        return str(self.ano)

    class Meta:
        verbose_name = "Rendimento escolar"
        verbose_name_plural = "Rendimentos escolares"
