# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from Pessoas.models import Aluno,  Perfil_do_Aluno
from .models import Rendimento, Dificuldade_por_disciplina
from django.shortcuts import render
from Pessoas.views import TipoAluno
from datetime import date
# Create your views here.

def censo_alunos(request):
    alunos = Perfil_do_Aluno.objects.all()
    #local de residencia
    qtd_urbano = Perfil_do_Aluno.objects.filter(reside="Urbano").count()
    qtd_agricola = Perfil_do_Aluno.objects.filter(reside="Agrícola").count()
    qtd_alunos_local = list()
    qtd_alunos_local.append(qtd_urbano)
    qtd_alunos_local.append(qtd_agricola)

    #objetivos
    obj_1 = Perfil_do_Aluno.objects.filter(objetivos='Curso superior na área agrícola').count()
    obj_2 = Perfil_do_Aluno.objects.filter(objetivos='Curso superior fora da área agrícola').count()
    obj_3 = Perfil_do_Aluno.objects.filter(objetivos='Continuar trabalho familiar na agricultura').count()
    obj_4 = Perfil_do_Aluno.objects.filter(objetivos='Trabalhar na área do curso').count()
    obj_5 = Perfil_do_Aluno.objects.filter(objetivos='Outro').count()
    obj_6 = Perfil_do_Aluno.objects.filter(objetivos='Não sabe responder').count()
    objetivos = list()
    objetivos.append(obj_1)
    objetivos.append(obj_2)
    objetivos.append(obj_3)
    objetivos.append(obj_4)
    objetivos.append(obj_5)
    objetivos.append(obj_6)


    #motivacao
    mot_1 = Perfil_do_Aluno.objects.filter(motivo='Ensino Médio de qualidade').count()
    mot_2 = Perfil_do_Aluno.objects.filter(motivo='Curso técnico').count()
    mot_3 = Perfil_do_Aluno.objects.filter(motivo='Ambos').count()
    mot_4 = Perfil_do_Aluno.objects.filter(motivo='Outro').count()
    motivacao = list()
    motivacao.append(mot_1)
    motivacao.append(mot_2)
    motivacao.append(mot_3)
    motivacao.append(mot_4)

    #tipo de aluno
    tipo = TipoAluno()
    aluno_A = [al for al in alunos if tipo.avaliar(al.nota_ensino, al.nota_comportamento) > 6.5 ]
    aluno_B = [ al for al in alunos if tipo.avaliar(al.nota_ensino, al.nota_comportamento) > 4.6 and
        tipo.avaliar(al.nota_ensino, al.nota_comportamento) <= 6.5  ]
    aluno_C = [ al for al in alunos if tipo.avaliar(al.nota_ensino, al.nota_comportamento) < 4.6]

    aluno_A = len(aluno_A)
    aluno_B = len(aluno_B)
    aluno_C = len(aluno_C)

    alunos_ABC = list()
    alunos_ABC.append(aluno_A)
    alunos_ABC.append(aluno_B)
    alunos_ABC.append(aluno_C)



    context = {
        'qtd_alunos_local':json.dumps(qtd_alunos_local),
        'objetivos':json.dumps(objetivos),
        'motivacao':json.dumps(motivacao),
        'alunos_ABC':json.dumps(alunos_ABC),
    }

    return render(request, 'censo_alunos.html', context)

def censo_rendimento(request):
    alunos = Aluno.objects.all()
    #rendimento por ano
    apro_s = list()
    apro_c = list()
    com_dep = list()
    repro = list()
    ren_anos = list()
    anos = Rendimento.objects.all().order_by('ano')
    for i in xrange(len(anos)):
        ren_anos.append(anos[i].ano)
        apro_s.append(anos[i].aprovados_sem_exame)
        apro_c.append(anos[i].aprovados_com_exame)
        com_dep.append(anos[i].com_dependencia)
        repro.append(anos[i].reprovados)

    #rendimento anterior
    ano_anterior = (date.today().year)-1
    queryset = Rendimento.objects.filter(ano=ano_anterior)
    aprovados_s = [aps.aprovados_sem_exame for aps in queryset ]
    aprovados_c = [aps.aprovados_com_exame for aps in queryset ]
    com_dependencia = [aps.com_dependencia for aps in queryset ]
    reprovados = [aps.reprovados for aps in queryset ]


    #dificuldades
    censo_dificuldades = Dificuldade_por_disciplina.objects.all().order_by('-numero_de_alunos')
    disciplina = [d.disciplina for d in censo_dificuldades ]
    qtd_al = [q.numero_de_alunos for q in censo_dificuldades]

    #movimento
    falecidos = [al.nome for al in alunos if al.faleceu == True]
    transferidos = [al.nome for al in alunos if al.transferido == True]
    abandonos = [al.nome for al in alunos if al.abandonou == True]

    movimento = list()
    movimento.append(len(falecidos))
    movimento.append(len(transferidos))
    movimento.append(len(abandonos))

    context = {
        'aprovados_s':json.dumps(aprovados_s),
        'aprovados_c':json.dumps(aprovados_c),
        'com_dependencia':json.dumps(com_dependencia),
        'reprovados':json.dumps(reprovados),
        'disciplina':json.dumps(disciplina),
        'qtd_al':json.dumps(qtd_al),
        'ano_anterior':ano_anterior,
        'movimento':json.dumps(movimento),
        'ren_anos':json.dumps(ren_anos),
        'apro_s':json.dumps(apro_s),
        'apro_c':json.dumps(apro_c),
        'com_dep':json.dumps(com_dep),
        'repro':json.dumps(repro),
    }

    return render(request, 'censo_rendimento.html', context)


def censo_cidades(request):
    #cidades
    alunos = Aluno.objects.all()
    cidades = [obj.cidade for obj in alunos]
    dic_qtd_alunos = {cit:cidades.count(cit) for cit in set(cidades)}
    cidades = dic_qtd_alunos.keys()
    qtd_alunos = dic_qtd_alunos.values()

    context = {
        'cidades':json.dumps(cidades),
        'qtd_alunos':json.dumps(qtd_alunos),
    }

    return render(request, 'censo_cidade.html', context)
