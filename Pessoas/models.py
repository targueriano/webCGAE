# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.
class Pessoa(models.Model):
    matricula = models.PositiveIntegerField('Matrícula', primary_key=True)
    nascimento = models.DateField(editable=True, blank=True, null=True)
    telefone = models.CharField("Telefone do aluno", max_length=20, blank=True, null=True, default='(Nenhum)', help_text='4798877-6655')

    class Meta:
        abstract = True

    def __str__(self):
        return '%s'%self.matricula


class Perfil_do_Servidor(Pessoa):
    CARREIRA = (
        (u'Docente',u'Docente'),
        (u'Técnico Administrativo', u'Técnico Administrativo'),
        (u'Tercerizado', u'Tercerizado'),
    )
    servidor = models.OneToOneField(User, related_name='servidor')
    carreira = models.CharField(choices=CARREIRA, max_length=50, default="Técnico Administrativo")
    cargo = models.CharField(max_length=100, default="Assistente de alunos")

    class Meta:
        verbose_name = 'Perfil do servidor'
        verbose_name_plural = 'Perfil dos servidores'


class Curso(models.Model):
    curso = models.CharField(max_length=100)


    def __str__(self):
        return self.curso

    def __unicode__(self):
	    return self.curso



class Turma(models.Model):
    curso  = models.ForeignKey(Curso)
    turma = models.CharField(max_length=10, primary_key=True)


    def __str__(self):
        return self.turma

    def __unicode__(self):
	    return self.turma


class Aluno(Pessoa):

    ALOJA = (
        (u'1A',u'1A'),
        (u'1B',u'1B'),
        (u'1C',u'1C'),
        (u'1D',u'1D'),
        (u'1E',u'1E'),
        (u'1F',u'1F'),
        (u'2A',u'2A'),
        (u'2B',u'2B'),
        (u'2C',u'2C'),
        (u'2D',u'2D'),
        (u'2E',u'2E'),
        (u'2F',u'2F'),
        (u'3A',u'3A'),
        (u'3B',u'3B'),
        (u'3C',u'3C'),
        (u'3D',u'3D'),
        (u'3E',u'3E'),
        (u'3F',u'3F'),
        (u'4A',u'4A'),
        (u'4B',u'4B'),
        (u'4C',u'4C'),
        (u'4D',u'4D'),
        (u'4E',u'4E'),
        (u'4F',u'4F'),
        (u'5A',u'5A'),
        (u'5B',u'5B'),
        (u'5C',u'5C'),
        (u'5D',u'5D'),
        (u'5E',u'5E'),
        (u'5F',u'5F'),
        (u'6A',u'6A'),
        (u'6B',u'6B'),
        (u'6C',u'6C'),
        (u'6D',u'6D'),
        (u'6E',u'6E'),
        (u'6F',u'6F'),
        (u'7A',u'7A'),
        (u'7B',u'7B'),
        (u'7C',u'7C'),
        (u'7D',u'7D'),
        (u'7E',u'7E'),
        (u'7F',u'7F'),
        (u'8A',u'8A'),
        (u'8B',u'8B'),
        (u'8C',u'8C'),
        (u'8D',u'8D'),
        (u'8E',u'8E'),
        (u'8F',u'8F'),
        (u'9A',u'9A'),
        (u'9B',u'9B'),
        (u'9C',u'9C'),
        (u'9D',u'9D'),
        (u'9E',u'9E'),
        (u'9F',u'9F'),
        (u'10A',u'10A'),
        (u'10B',u'10B'),
        (u'10C',u'10C'),
        (u'10D',u'10D'),
        (u'10E',u'10E'),
        (u'10F',u'10F'),
        (u'11A',u'11A'),
        (u'11B',u'11B'),
        (u'11C',u'11C'),
        (u'11D',u'11D'),
        (u'11E',u'11E'),
        (u'11F',u'11F'),
        (u'12A',u'12A'),
        (u'12B',u'12B'),
        (u'12C',u'12C'),
        (u'12D',u'12D'),
        (u'12E',u'12E'),
        (u'12F',u'12F'),
        (u'13A',u'13A'),
        (u'13B',u'13B'),
        (u'13C',u'13C'),
        (u'13D',u'13D'),
        (u'13E',u'13E'),
        (u'13F',u'13F'),
        (u'14A',u'14A'),
        (u'14B',u'14B'),
        (u'14C',u'14C'),
        (u'14D',u'14D'),
        (u'14E',u'14E'),
        (u'14F',u'14F'),
        (u'15A',u'15A'),
        (u'15B',u'15B'),
        (u'15C',u'15C'),
        (u'15D',u'15D'),
        (u'15E',u'15E'),
        (u'15F',u'15F'),
        (u'ZooI',u'ZooI'),
        (u'ZooII',u'ZooII'),
        (u'ZooIII',u'ZooIII'),
    )
    nome = models.CharField(max_length=100, help_text="Nome completo do aluno")
    cidade = models.CharField(max_length=60, editable=True, blank=True, null=True)
    turma = models.ForeignKey(Turma)
    alojamento = models.CharField(max_length=10, null=True, blank=True, editable=True, choices=ALOJA)
    emancipado = models.BooleanField(default=False)
    transferido = models.BooleanField(default=False)
    abandonou = models.BooleanField(default=False)
    faleceu = models.BooleanField(default=False)


    class Meta:
        ordering = ['nome']
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def get_absolute_url(self):
        return reverse('aluno_lista')

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return self.nome

class Familia(models.Model):
    aluno = models.OneToOneField(Aluno, primary_key=True)
    pai = models.CharField(max_length=80, blank=True, null=True)
    profissao_pai = models.CharField("Profissão do pai", max_length=80, blank=True, null=True)
    mae = models.CharField('Mãe', max_length=80, blank=True, null=True)
    profissao_mae = models.CharField("Profissão da mãe", max_length=80, blank=True, null=True)
    responsavel = models.CharField('Responsável', max_length=80, blank=True, null=True)
    telefone = models.CharField("Telefone residencial", help_text='4799878-6788',
                                blank=False, max_length=20, null=True, default='(Nenhum)')
    telefone2 = models.CharField(help_text='479999-9999', blank=False,
                               max_length=20, null=True, default='(Nenhum)')
    telefone3 = models.CharField(help_text='479999-9999', blank=False,
                                max_length=20, null=True, default='(Nenhum)')

    def __str__(self):
        return str(self.aluno)

    class Meta:
        ordering = ['aluno']
        verbose_name = "Família do aluno"
        verbose_name_plural = "Família de cada aluno"

    def get_absolute_url(self):
        return reverse('aluno_lista')

class Perfil_do_Aluno(models.Model):
    LOCAL = (
        ('Agrícola', 'Agrícola'),
        ('Urbano', 'Urbano'),
    )
    MOT = (
        (u'Ensino Médio de qualidade', u'Ensino Médio de qualidade'),
        (u'Curso técnico', u'Curso técnico'),
        (u'Ambos', u'Ambos'),
        (u'Outro', u'Outro'),
    )
    OBJ = (
        (u'Curso superior na área agrícola', u'Curso superior na área agrícola'),
        (u'Curso superior fora da área agrícola', u'Curso superior fora da área agrícola'),
        (u'Continuar trabalho familiar na agricultura', u'Continuar trabalho familiar na agricultura'),
        (u'Trabalhar na área do curso', u'Trabalhar na área do curso'),
        (u'Outro', u'Outro'),
        (u'Não sabe responder', u'Não sabe responder'),

    )
    FORMA = (
        (u'Integrado',u'Integrado'),
        (u'Subsequente',u'Subsequente'),
        (u'Bacharelado',u'Bacharelado'),
        (u'Engenharia',u'Engenharia'),
        (u'Licenciatura',u'Licenciatura'),
    )
    aluno = models.OneToOneField(Aluno, primary_key=True, related_name='perfil_aluno')
    nota_ensino = models.FloatField("Nota de ensino", blank=True, default=7.0, max_length=4, editable=True, null=True)
    nota_comportamento = models.FloatField("Nota de comportamento", blank=True, default=7.0, max_length=4, editable=True, null=True)
    saude = models.CharField('Saúde', max_length=300, default=None, blank=True, editable=True, null=True)
    reside = models.CharField("Reside em local", max_length=10, choices=LOCAL)
    objetivos = models.CharField(max_length=300, choices=OBJ, help_text="Objetivo ao completar o curso", null=True, blank=True)
    foto = models.ImageField(upload_to='Pessoas/', null=True, blank=True, help_text="O nome do arquivo não pode conter acentos.")
    motivo = models.CharField(max_length=100, choices=MOT, help_text="Motivo pela escolha do IFC", null=True, blank=True)
    curso = models.ForeignKey(Curso)
    forma = models.CharField(choices=FORMA, max_length=30)

    class Meta:
        ordering = ['aluno']
        verbose_name = "Perfil do aluno"
        verbose_name_plural = "Perfil dos alunos"

    def __str__(self):
        return str(self.aluno)

    def get_absolute_url(self):
        return reverse('aluno_lista')
