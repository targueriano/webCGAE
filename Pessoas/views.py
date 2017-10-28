# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Aluno
from django.views.generic import CreateView, UpdateView
from Pessoas.models import Aluno, Curso, Familia, Perfil_do_Aluno
from Atividades.models import (Vistoria, Prontuario,Comunicados, Escala_Limpeza,
                                       Escala_Servidores, Limpeza, Relatorio,
                                       Educacional, Educacional_detalhe)
from datetime import date
from django.http import Http404
from django.db.models import F
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Create your views here.

class RequerPoder(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if (not request.user.has_perm('add_aluno') or not request.user.has_perm('add_curso_do_aluno')
            or not request.user.has_perm('add_familia_do_aluno') or not request.user.has_perm('add_perfil_do_aluno')):
            return redirect('/accounts/login/')
        return super(RequerPoder, self).dispatch(request, *args, **kwargs)


class Aluno_update(RequerPoder, UpdateView):
    model = Aluno
    fields = '__all__'


class Aluno_add(RequerPoder, CreateView):
    model = Aluno
    fields = ('matricula', 'nome', 'nascimento', 'telefone', 'cidade', 'turma', 'alojamento', 'emancipado')
    success_url = 'sucesso'


class Aluno_add_perfil(RequerPoder, CreateView):
    model = Perfil_do_Aluno
    fields = '__all__'
    success_url = reverse_lazy('sucesso')



class Aluno_update_perfil(RequerPoder, UpdateView):
    model = Perfil_do_Aluno
    fields = '__all__'



class Aluno_add_familia(RequerPoder, CreateView):
    model = Familia
    fields = '__all__'
    success_url = reverse_lazy('sucesso')



class Aluno_update_familia(RequerPoder, UpdateView):
    model = Familia
    fields = '__all__'


class Aluno_add_curso(RequerPoder, CreateView):
    model = Curso
    fields = '__all__'
    success_url = reverse_lazy('sucesso')



class Aluno_update_curso(RequerPoder, UpdateView):
    model = Curso
    fields = '__all__'


class TipoAluno():
    """
    Logica fuzzy para avaliar o tipo de aluno
    """
    def __init__(self):
        nota, comportamento, tipoaluno = self._definirVariaveis()
        nota, comportamento, tipoaluno = self._definirPertinencia(nota, comportamento, tipoaluno)
        self.tipo = self._definirRegras(nota, comportamento, tipoaluno)


    def avaliar(self, nota, comportamento ):
        self.tipo.input['nota'] = nota
        self.tipo.input['comportamento'] = comportamento
        self.tipo.compute()

        return self.tipo.output['tipoaluno']

    def _definirVariaveis(self):
        nota = ctrl.Antecedent(np.arange(0, 11, 1), 'nota')
        comportamento = ctrl.Antecedent(np.arange(0, 11, 1), 'comportamento')
        tipoaluno = ctrl.Consequent(np.arange(0, 11, 1), 'tipoaluno')

        return nota,comportamento,tipoaluno

    def _definirPertinencia(self, nota, comportamento, tipoaluno):
        nota['low'] = fuzz.trapmf(nota.universe, [0, 0, 0, 5 ])
        nota['medium'] = fuzz.trimf(nota.universe, [2, 5, 8])
        nota['high'] = fuzz.trapmf(nota.universe, [5, 8, 10, 11])

        comportamento['low'] = fuzz.trapmf(comportamento.universe, [0, 0, 0, 5 ])
        comportamento['medium'] = fuzz.trimf(comportamento.universe, [2, 5, 8])
        comportamento['high'] = fuzz.trapmf(comportamento.universe, [5, 8, 10, 11])

        tipoaluno['C'] = fuzz.trapmf(tipoaluno.universe, [0, 0, 0, 5 ])
        tipoaluno['B'] = fuzz.trimf(tipoaluno.universe, [2, 5, 8])
        tipoaluno['A'] = fuzz.trapmf(tipoaluno.universe, [5, 8, 10, 11])

        return nota,comportamento,tipoaluno

    def _definirRegras(self, nota, comportamento, tipoaluno):
        rule1 = ctrl.Rule(nota['low'] & comportamento['low'], tipoaluno['C'])
        rule2 = ctrl.Rule(nota['low'] & comportamento['medium'], tipoaluno['C'])
        rule3 = ctrl.Rule(nota['low'] & comportamento['high'], tipoaluno['B'])
        rule4 = ctrl.Rule(nota['medium'] & comportamento['low'], tipoaluno['C'])
        rule5 = ctrl.Rule(nota['medium'] & comportamento['medium'], tipoaluno['B'])
        rule6 = ctrl.Rule(nota['medium'] & comportamento['high'], tipoaluno['B'])
        rule7 = ctrl.Rule(nota['high'] & comportamento['low'], tipoaluno['C'])
        rule8 = ctrl.Rule(nota['high'] & comportamento['medium'], tipoaluno['B'])
        rule9 = ctrl.Rule(nota['high'] & comportamento['high'], tipoaluno['A'])

        tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3,
								   rule4, rule5, rule6,
								   rule7, rule8, rule9
								  ])


        tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

        return tipping

def home(request):
    alunos = Aluno.objects.all().order_by('turma')
    count_alunos = Aluno.objects.count()
    count = Relatorio.objects.count()

    count_com = Comunicados.objects.count()
    count_pront = Prontuario.objects.count()
    count_edu = Educacional.objects.count()

    count_total = count_com + count_pront + count_edu
    top_ensino = Perfil_do_Aluno.objects.all().order_by('-nota_ensino')[:20]
    top_comportamento = Perfil_do_Aluno.objects.all().order_by('-nota_comportamento')[:20]



    context = {'alunos':alunos,
               'count_alunos':count_alunos,
               'count':count,
               'count_total':count_total,
               'top_ensino':top_ensino,
               'top_comportamento':top_comportamento,

               }

    return render(request, 'home.html', context)

def fotovisor(request):
    return render(request, 'Pessoas/fotovisor.html',)


def fotovisor_turma(request, turma):
    turma = turma
    alunos = Aluno.objects.filter(turma=turma)

    context = {'alunos':alunos,
               'turma':turma}
    return render(request, 'Pessoas/fotovisor_turma.html', context )


def lista_alunos(request):
    alunos = Aluno.objects.all()

    var_get_search = request.POST.get('search_box')

    if var_get_search is not None:
        alunos = alunos.filter(
              Q(nome__icontains=var_get_search)
            | Q(matricula__contains=var_get_search)
            | Q(cidade=var_get_search)
            | Q(alojamento=var_get_search)
        )

    paginator = Paginator(alunos, 50)

    # Esteja certo de que o `page request` é um inteiro. Se não, mostre a primeira página.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        alunos = paginator.page(page)
    except (EmptyPage, InvalidPage):
        alunos = paginator.page(paginator.num_pages)


    context = {
        'alunos':alunos,
    }
    return render(request, 'Pessoas/alunos_lista.html', context)


def alojamento(request):
    aloja = [
             '1A', '1B', '1C', '1D', '1E', '1F',
             '2A', '2B', '2C', '2D', '2E', '2F',
             '4A', '4B', '4C', '4D', '4E', '4F',
             '5A', '5B', '5C', '5D', '5E', '5F',
             '6A', '6B', '6C', '6D', '6E', '6F',
             '7A', '7B', '7C', '7D', '7E', '7F',
             '8A', '8B', '8C', '8D', '8E', '8F',
             '9A', '9B', '9C', '9D', '9E', '9F',
             '10A', '10B', '10C', '10D', '10E', '10F',
             '11A', '11B', '11C', '11D', '11E', '11F',
             '12A', '12B', '12C', '12D', '12E', '12F',
             '13A', '13B', '13C', '13D', '13E', '13F',
             '14A', '14B', '14C', '14D', '14E', '14F',
             '15A', '15B', '15C', '15D', '15E', '15F',
    ]



    lista = list()

    for i in xrange(14*6):
        cont = Aluno.objects.filter(alojamento=aloja[i]).count()
        lista.append(cont)


    context = {
        'lista':lista,

    }
    return render(request, 'Pessoas/alojamento.html', context)

def alojamento_quarto(request, pk):
    alunos = Aluno.objects.filter(alojamento=pk)

    context = {
        'alunos':alunos,
    }
    return render(request, 'Pessoas/alojamento_quarto.html', context)

def perfil_aluno(request, pk):
    aluno = Aluno.objects.get(pk=pk)
    perfil = Perfil_do_Aluno.objects.filter(aluno=pk)


    #verifica se eh servidor ou outro para disponibilizar dados conforme o resultado
    if request.user.is_anonymous():
        comunicados = Comunicados.objects.filter(aluno=pk).values('id','tipo', 'aluno', 'data', 'servidor')
        relatorios = Relatorio.objects.filter(denunciado=pk).values('id','titulo', 'artigo','medida_prevista',
        'data', 'servidor')
        educacional = Educacional_detalhe.objects.filter(educacional=pk).values('setor', 'data', 'servidor')
    else:
        relatorios = Relatorio.objects.filter(denunciado=pk).order_by('-data')
        comunicados = Comunicados.objects.filter(aluno=pk).order_by('-data')
        educacional = Educacional_detalhe.objects.filter(educacional=pk)

    """Calcula a idade do aluno"""
    try:
        data_hj = date.today()
        idade = data_hj.year - aluno.nascimento.year - ((data_hj.month, data_hj.day) < (aluno.nascimento.month, aluno.nascimento.day))
    except:
        idade = 0


    if aluno.emancipado:
        emancipado = "SIM"
    else:
        emancipado = "NÃO"

    """Chama a classe para avaliar o tipo de aluno """
    tipo = TipoAluno()

    if perfil:
        valor = tipo.avaliar(aluno.perfil_aluno.nota_ensino, aluno.perfil_aluno.nota_comportamento)
    else:
        valor = 6.5

    #calcular posicao no rank de ensino e de comportamento
    alunos_ensino = Perfil_do_Aluno.objects.all().order_by('-nota_ensino')
    alunos_comportamento = Perfil_do_Aluno.objects.all().order_by('-nota_comportamento')

    posicao_ensino = 0
    posicao_comportamento = 0
    i = 1
    for a in alunos_ensino:
        if a.aluno == aluno:
            posicao_ensino = i
        i += 1

    i = 1
    for a in alunos_comportamento:
        if a.aluno == aluno:
            posicao_comportamento = i
        i += 1

    context = {'aluno': aluno,
               'valor':valor,
               'emancipado':emancipado,
               'idade': idade,
               'posicao_ensino':posicao_ensino,
               'posicao_comportamento':posicao_comportamento,
               'relatorios':relatorios,
               'comunicados':comunicados,
               'educacional':educacional,
               }

    return render(request, 'Pessoas/perfil_aluno.html', context)


def aluno_add_sucesso(request):
    return render(request, 'Pessoas/aluno_add_sucesso.html', )
