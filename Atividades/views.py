# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from Pessoas.models import Aluno, Curso
from .forms import (ComunicadoForm, RelatorioForm, ProntuarioDetalheForm,
                              ProntuarioForm, Prontuario_detalhe_formset,
                              Educacional_detalhe_formset, EducacionalForm)
from .models import (Vistoria, Comunicados, Prontuario, Relatorio,
                                Escala_Limpeza, Escala_Servidores,
                                Limpeza, Prontuario_detalhe, Educacional,
                                 Educacional_detalhe)

from django.views.generic import CreateView, UpdateView, ListView, DetailView
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import redirect
from django.utils import timezone
from datetime import date
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.graphics.shapes import Line, Drawing
from reportlab.lib.units import cm, inch
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.forms import inlineformset_factory
from datetime import date
from django.core.files.storage import FileSystemStorage
import os.path
from django.db import transaction
from django.contrib.auth.mixins import AccessMixin


MESES = ('janeiro','fevereiro','março','abril','maio','junho',
       'julho','agosto','setembro','outubro','novembro','dezembro')


REGULAMENTO = ("""Art.18, inciso I, faltar com asseio pessoal e organização
    dos seus pertences e dos recursos e/ou equipamentos do IFC sob sua
    responsabilidade ou uso""","""Art.18, inciso II, descumprir o horário geral das
    atividades do campus""","""Art.18, inciso III, proferir palavras obscenas ou ofensivas""",
    """Art.18, inciso IV, fazer gestos obscenos""","""Art.18, inciso V, não cumprir as escalas de atividades
    pedagógicas curriculares optativas""","""Art.18, inciso VI, descumprir as normas do campus que
    orientam o uso de instalações e serviços""","""Art.18, inciso VII, manter-se em
    atitude de desinteresse ou com vistas à desordem das atividaes pedagógicas""",
    """Art.18, inciso VIII, incumbir outra pessoa do desempenho de tarefa que seja
    de sua responsabilidade""","""Art.18, inciso IX, apresentar-se sem uniforme nas atividades
    pedagógicas, caso as normas estabelecidas pelo campus instituam a necessidade
    de seu uso""","""Art.18, inciso X, entrar nas dependências do IFC sem autorização
    ou identificação, caso as normas estabelecidas pelo campus instituam essa
    necessidade""","""Art.18, inciso XI, ter outros comportamentos, não constantes
    nesse rol, que podem ser equiparados, pelo CAE/CGAE do campus ou pela
    coordenação de curso, aos atos aqui arrolados(REVOGADO)""",
    """Art.19, inciso I, ausentar-se da sala de aula ou das dependências do IFC
    sem autorização, caso as normas estabelecidas pelo campus instituam essa
    necessidade""","""Art.19, inciso II, omitir-se, sem justificativa, de programações
    esportivas, cívicas, artísticas e culturais, e viagens acadêmicas
    quando estiver representando o campus dentro ou fora do IFC""",
    """Art.19, inciso III, descumprir as tarefas pedagógicas,
    sem justificativas previstas em lei""","""Art.19, inciso IV, usar de meios ilícitos durante
    realização de atividades avaliativas""", """Art.19, inciso V, usar
    de desonestidade para eximir-se das atividades pedagógicas""","""Art.19, inciso VI, omitir
    ou distorcer informações quando solicitadas""","""Art.19, inciso VII, utilizar o telefone celular ou outro equipamento
    eletrônico que interfira no bom andamento das atividades pedagógicas, salvo
    os casos [...] autorizados [...]""","""Art.19, inciso VIII, efetuar transação comercial, inclusive
    rifas e sorteios, dentro do campus, sem a devida autorização""",
    """Art.19, inciso IX, apresentar comportamentos ou vestimentas que atentem ao pudor""",
    """Art.19, inciso X, fazer uso indevido de recursos tecnológicos
    (redes sociais, mensagens instantâneas, sites em geral, e-mail, entr outros),
    de forma a infringir o presente Regulamento""","""Art.19, inciso XI, negligenciar o cuidado com  os animais sob sua
    responsabilidade""","""Art.19, inciso XII, adentrar e permanecer, em sala de aula
    e/ou outros locais fechados, nas dependências do IFC, com animais[...]""",
    """Art.19, inciso XIII, adentrar e permanecer nos locais
    de atividades pedagógicas com pessoas não-matriculadas, sem autorização
    prévia do(a) docente ou coordenador(a) responsável""","""Art.19, inciso XIV, ter outros comportamentos, não constantes
    nesse rol, que podem ser equiparados, pelo CAE/CGAE do campus ou pela
    coordenação de curso, aos atos aqui arrolados (REVOGADO)""",
    """Art.20, inciso I, usar barragens, rios, lagos e açudes, do campus
    e proximidades, para banho, pesca ou outras atividades afins sem autorização""",
    """Art.20, inciso II, recusar-se a seguir as normas de segurança do trabalho
    nas aulas de laboratório, e/ou de campo, e visitas técnicas""",
    """Art.20, inciso III, organizar e/ou praticar trote em discentes
    sem a autorização da Coordenação do curso""",
    """Art.20, inciso IV, portar ou depositar bebida alcoólica, cigarros ou
    outras drogras lícitas, nas dependências do IFC, se maior de idade""",
    """Art.20, inciso V, ter outros comportamentos, não constantes
    nesse rol, que podem ser equiparados, pelo CAE/CGAE do campus ou pela
    coordenação de curso, aos atos aqui arrolados (REVOGADO)""",
    """Art.21, inciso I, coagir outra pessoa a qualquer atitude
     contrária a sua vontade""","""Art.21, inciso II, coagir membro da comunidade do IFC
    ou qualquer visitante à prática de atos atentatórios à Lei""","""Art.21, inciso III, furtar, ou sua tentativa""",
    """Art.21, inciso IV, roubar, ou sua tentativa""","""Art.21, inciso V, portar ou usar qualquer espécie de arma""",
    """Art.21, inciso VI, tentar agredir ou agredir física e/ou
     moralmente qualquer pessoa, nas depências do IFC ou em âmbito
     externo, quando em atividades pedagógicas ou em representação
     do IFC""","""Art.21, inciso VII, expor, intencionalmente ou não,
    a perigo a vida ou saúde de outrem""",
    """Art.21, inciso VIII, praticar atos libidinosos ou obscenos""","""Art.21, inciso IX, ameaçar alguém oralmente, por escrito,
    por meio de gestos ou qualquer outro meio simbólico""","""Art.21, inciso X, deixar de prestar assistência à pessoa
    ameaçada, constrangida ou exposta a iminente perigo, ou, quando
    não for possível fazê-lo sem risco à própria integridade física, não
    solicitar o socorro devido""","""Art.21, inciso XI, usar de maneira indevida os diferentes espaços
    do campus, colocando em risco a integridade própria e/ou de
    terceiros""","""Art.21, inciso XII, praticar atos atentatórios
    à dignidade [...]""","""Art.21, inciso XIII, aplicar trotes atentatórios
    à dignidade ou que coloquem em risco à vida de outrem""","""Art.21, inciso XIV, praticar, induzir ou incitar,
    por qualquer meio, a discriminação ou o preconceito [...]""",
    """Art.21, inciso XV, praticar toda e qualquer ação de
    intimidação, agressões intencionais, verbais ou físicas feitas
    de maneira repetitiva, que configure a prática de bullying""",
    """Art.21, inciso XVI, praticar violência ou abuso
    contra animais, ou qualquer outra forma de violação das leis vigentes""",
    """Art.21, inciso XVII, portar ou depositar bebida alcoólica,
    cigarros ou outras drogas lícitas, nas dependências do IFC, se menor de idade""",
    """Art.21, inciso XVIII, portar ou depositar drogas
    ilícitas nas dependências do IFC""","""Art.21, inciso XIX, usar ou incentivar o uso de
    drogas lícitas e ilícitas, ou apresentar sintomas de seu
    uso, nas dependências do IFC ou externamente, em atividades
    executadas pelo IFC, de que o (a) discente faça parte""",
    """Art.21, inciso XX, comercializar, fornecer, servir,
     ministrar ou entregar bebida alcoólica, cigarro ou outras
     drogas lícitas e ilícitas, dentro do IFC, em atividade
     pedagógica ou atividade em que estiver representando o IFC""",
     """Art.21, inciso XXI, adulterar ou falsificar pareceres
    ou documentos""","""Art.21, inciso XXII, recorrer a meios fraudulentos para lograr
    vantagem para si ou para outrem""","""Art.21, inciso XXIII, utilizar pessoal ou recursos
    materiais do IFC em serviços ou atividades particulares""","""Art.21, inciso XXIV, depredar o patrimônio público
    ou privado""","""Art.21, inciso XXV, promover ou participar de atos de
    vandalismo""","""Art.21, inciso XXVI, praticar a retirada de equipamentos,
    produtos e outros itens que constituem patrimônio do IFC,
    sem a prévia autorização de seus responsáveis""","""Art.21, inciso XXVII, cometer plágio, ou seja,
    apropriar-se, parcialmente ou na íntegra, do trabalho de outrem
    e utilizá-lo como se fosse seu, sem lhe dar o devido crédito,
    ou seja, sem citá-lo como fonte""","""Art.21, inciso XXVIII, usar de forma indevida o
    nome ou o símbolo do IFC, sendo agravante o uso a fim de
    tirar proveito, para si ou para outrem, ou a fim de difamar a instituição""",
    """Art.21, inciso XXIX, promover eventos usando o
    nome do IFC sem a devida autorização da Direção""",
    """Art.21, inciso XXX,  divulgar, ceder ou comercializar
    dados relativos a pesquisas do IFC, sem a autorização de
    autoridade competente""","""Art.21, inciso XXXI, devassar o conteúdo ou se
    apossar indevidamente de correspondência alheia""",
    """Art.21, inciso XXXII, acessar computadores, softwares,
    dados, informações, redes ou porções restritas do sistema
    computacional do IFC, sem a devida autorização""",
    """Art.21, inciso XXXIII, enviar spams, mensagens
    fraudulentas, pornográficas ou ameaçadoras""",
    """Art.21, inciso XXXIV, outros, não constantes
    neste rol, que se caracterizem como infrações (REVOGADO)"""
    )


class RequerPoderAmbulatorial(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('Atividades.add_prontuario'):
            return redirect('/accounts/login/')

        return super(RequerPoderAmbulatorial, self).dispatch(request, *args, **kwargs)

class RequerPoderEducacional(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('Atividades.add_educacional'):
            return redirect('/accounts/login/')

        return super(RequerPoderEducacional, self).dispatch(request, *args, **kwargs)

class RequerPoderComunicativo(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('Atividades.add_comunicado'):
            return redirect('/accounts/login/')

        return super(RequerPoderComunicativo, self).dispatch(request, *args, **kwargs)


class RequerPoderLegislativo(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('Atividades.add_relatorio'):
            return redirect('/accounts/login/')

        return super(RequerPoderLegislativo, self).dispatch(request, *args, **kwargs)


# Create your views here.
class Prontuario_update(RequerPoderAmbulatorial, UpdateView):
    model = Prontuario
    success_url = "prontuario_lista"
    fields = '__all__'


class Prontuario_detalhe_update(RequerPoderAmbulatorial, UpdateView):
    model = Prontuario
    fields = '__all__'
    success_url = reverse_lazy('prontuario_lista')

    def get_context_data(self, **kwargs):
        data = super(Prontuario_detalhe_update, self).get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = Prontuario_detalhe_formset(self.request.POST, instance=self.object)
        else:
            data['formset'] = Prontuario_detalhe_formset(instance=self.object)

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        pd_detalhe = context['formset']
        with transaction.atomic():
            self.object = form.save()

            if pd_detalhe.is_valid():
                pd_detalhe.instance = self.object
                pd_detalhe.save()

        return super(Prontuario_detalhe_update, self).form_valid(form)


class Comunicado_update(RequerPoderComunicativo, UpdateView):
    model = Comunicados
    fields = ('tipo', 'aluno', 'texto', 'servidor')


class Prontuario_add(RequerPoderAmbulatorial, CreateView):
    model = Prontuario
    fields = '__all__'
    success_url = reverse_lazy('prontuario_lista')

    def get_context_data(self, **kwargs):
        data = super(Prontuario_add, self).get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = Prontuario_detalhe_formset(self.request.POST)
        else:
            data['formset'] = Prontuario_detalhe_formset()

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        pd_detalhe = context['formset']
        with transaction.atomic():
            self.object = form.save()

            if pd_detalhe.is_valid():
                pd_detalhe.instance = self.object
                pd_detalhe.save()

        return super(Prontuario_add, self).form_valid(form)


class Educacional_add(RequerPoderEducacional, CreateView):
    model = Educacional
    fields = '__all__'
    success_url = reverse_lazy('educacional_lista')

    def get_context_data(self, **kwargs):
        data = super(Educacional_add, self).get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = Educacional_detalhe_formset(self.request.POST)
        else:
            data['formset'] = Educacional_detalhe_formset()

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        edu_detalhe = context['formset']
        with transaction.atomic():
            self.object = form.save()

            if edu_detalhe.is_valid():
                edu_detalhe.instance = self.object
                edu_detalhe.save()

        return super(Educacional_add, self).form_valid(form)


class Educacional_update(RequerPoderEducacional, UpdateView):
    model = Educacional
    fields = '__all__'
    success_url = "educacional_lista"

class Educacional_detalhe_update(RequerPoderEducacional, UpdateView):
    model = Educacional
    fields = '__all__'
    success_url = reverse_lazy('educacional_lista')

    def get_context_data(self, **kwargs):
        data = super(Educacional_detalhe_update, self).get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = Educacional_detalhe_formset(self.request.POST, instance=self.object)
        else:
            data['formset'] = Educacional_detalhe_formset(instance=self.object)

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        edu_detalhe = context['formset']
        with transaction.atomic():
            self.object = form.save()

            if edu_detalhe.is_valid():
                edu_detalhe.instance = self.object
                edu_detalhe.save()

        return super(Educacional_detalhe_update, self).form_valid(form)


class Relatorio_update(RequerPoderLegislativo, UpdateView):
    model = Relatorio
    fields = '__all__'
    exclude = ('data', 'controle',)


@login_required(login_url='/accounts/login/')
def comunicado_novo(request):
    if request.user.has_perm('Atividades.add_comunicados'):
        if request.method == 'POST':
            form = ComunicadoForm(request.POST)
            if form.is_valid():
                comunicado = form.save(commit=False)
                comunicado.data = timezone.now()
                comunicado.save()
                return redirect('comunicado_lista',)
        else:
            form = ComunicadoForm()

        return render(request, 'Atividades/comunicados_form.html', {'form':form})
    else:
        return redirect('/accounts/login/')


@login_required(login_url='/accounts/login/')
def prontuario_lista(request):
    prontuarios = Prontuario.objects.all()
    paginator = Paginator(prontuarios, 50)

    var_get_search = request.POST.get('search_box')

    if var_get_search is not None:
        prontuarios = prontuarios.filter(
              Q(aluno__nome__icontains=var_get_search)
        )

    # Esteja certo de que o `page request` é um inteiro. Se não, mostre a primeira página.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        prontuarios = paginator.page(page)
    except (EmptyPage, InvalidPage):
        prontuarios = paginator.page(paginator.num_pages)


    context = {
        'prontuarios':prontuarios,
    }

    return render(request, 'Atividades/prontuario_lista.html', context)


@login_required(login_url='/accounts/login/')
def prontuario_detalhe(request, pk):
    prontuario = Prontuario.objects.filter(aluno=pk)
    pd_detalhe = Prontuario_detalhe.objects.filter(prontuario=pk)


    context = {
        'prontuario':prontuario,
        'pd_detalhe':pd_detalhe,
    }
    return render(request, 'Atividades/prontuario_detalhe.html', context)


@login_required(login_url='/accounts/login/')
def educacional_lista(request):
    educacional = Educacional.objects.all()

    var_get_search = request.POST.get('search_box')

    if var_get_search is not None:
        educacional = educacional.filter(
              Q(aluno__nome__icontains=var_get_search)

        )

    paginator = Paginator(educacional, 50)

    # Esteja certo de que o `page request` é um inteiro. Se não, mostre a primeira página.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        educacional = paginator.page(page)
    except (EmptyPage, InvalidPage):
        educacional = paginator.page(paginator.num_pages)

    context = {
        'educacional':educacional,
    }

    return render(request, 'Atividades/educacional_lista.html', context)


@login_required(login_url='/accounts/login/')
def educacional_detalhe(request, pk):
    educacional = Educacional.objects.filter(aluno=pk)
    edu_detalhe = Educacional_detalhe.objects.filter(educacional=pk)


    context = {
        'educacional':educacional,
        'edu_detalhe':edu_detalhe,
    }
    return render(request, 'Atividades/educacional_detalhe.html', context)


def escala_limpeza(request):
    return render(request, 'Pessoas/escala_limpeza.html',)

def escala_limpeza_quarto(request, pk):
    quarto = pk.split(',')
    quartoAD = Escala_Limpeza.objects.filter(quarto=quarto[0])
    quartoBE = Escala_Limpeza.objects.filter(quarto=quarto[1])
    quartoCF = Escala_Limpeza.objects.filter(quarto=quarto[2])
    if len(quarto[0]) == 2:
        aloja = quarto[0][0]
        if quarto[0][1] == 'A':
            aloja += ' superior'
        else:
            aloja += ' inferior'
    else:
        aloja = quarto[0][0]+quarto[0][1]
        if quarto[0][2] == 'A':
            aloja += ' superior'
        else:
            aloja += ' inferior'

    context = {
        'quartoAD':quartoAD,
        'quartoBE':quartoBE,
        'quartoCF':quartoCF,
        'aloja':aloja,
    }

    return render(request, 'Pessoas/escala_limpeza_quarto.html', context)

def escala_cgae(request):
    data = date.today()
    dia = data.weekday()
    dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira')
    if dia > 4:
        dia = 0

    escala = Escala_Servidores.objects.filter(dia_da_semana=dias[dia]).order_by("horario_de_inicio")
    context = {
        'escala':escala,
        'dia':dia,
    }

    return render(request, 'Pessoas/escala_cgae.html', context)

def escala_cgae_select(request, pk):
    dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira')
    pk = int(pk)
    escala = Escala_Servidores.objects.filter(dia_da_semana=dias[pk]).order_by('horario_de_inicio')
    dia = pk
    context = {
        'escala':escala,
        'dia':dia,
    }

    return render(request, 'Pessoas/escala_cgae.html', context)


@login_required(login_url='/accounts/login/')
def lista_relatorios(request):
    relatorios = Relatorio.objects.all().order_by('-data')
    paginator = Paginator(relatorios, 50)
    #alunos = Aluno.objects.all()

    var_get_search = request.POST.get('search_box')

    if var_get_search is not None:
        relatorios = relatorios.filter(
              Q(data__icontains=var_get_search)
            | Q(denunciado__nome__icontains=var_get_search)
            | Q(medida_prevista__icontains=var_get_search)
            | Q(artigo__icontains=var_get_search)
            | Q(servidor__username__icontains=var_get_search)
            | Q(titulo__icontains=var_get_search)
        )

    # Esteja certo de que o `page request` é um inteiro. Se não, mostre a primeira página.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        relatorios = paginator.page(page)
    except (EmptyPage, InvalidPage):
        relatorios = paginator.page(paginator.num_pages)


    context = {'current_user': request.user,
               'relatorios': relatorios,
              }

    return render(request, 'Atividades/relatorio_lista.html', context)

@login_required(login_url='/accounts/login/')
def lista_vistorias(request):
    try:
        vistorias = Vistoria.objects.all().order_by('-data')
    except:
        vistorias = None

    var_get_search = request.POST.get('search_box')

    if var_get_search is not None:
        vistorias = vistorias.filter( Q(data__icontains=var_get_search)
            | Q(quarto__icontains=var_get_search)
        )

    return render(request, 'Functions/vistoria_lista.html', {'vistorias': vistorias})

@login_required(login_url='/accounts/login/')
def relatorio_detalhe(request, pk):
    relatorio = Relatorio.objects.get(pk=pk)
    try:
        aluno = Aluno.objects.get(matricula=relatorio.denunciado.matricula)
    except:
        aluno = None
    try:
        dados = Curso.objects.get(aluno=relatorio.denunciado)
    except:
        dados = None
    #efetuar a analise para avaliar o grau de andamento do processo
    cont = 0
    if relatorio.denuncia:
        cont += 25
    if relatorio.comunicado_discente:
        cont += 25
    if relatorio.protocolado:
        cont += 25
    if relatorio.medida_aplicada:
        cont += 25

    context = {
        'relatorio':relatorio,
        'aluno': aluno,
        'dados':dados,
        'cont':cont,
    }

    return render(request, 'Atividades/relatorio_detalhe.html', context)


@login_required(login_url='/accounts/login/')
def relatorio_novo(request):
    if request.user.has_perm('Atividades.add_relatorio'):
        if request.method == 'POST':
            form = RelatorioForm(request.POST)
            if form.is_valid():
                relatorio = form.save(commit=False)
                relatorio.data = timezone.now()
                relatorio.save()
                return redirect('relatorio_lista',)
        else:
            form = RelatorioForm()

        return render(request, 'Atividades/relatorio_form.html', {'form':form})
    else:
        return redirect('acesso_negado',)


@login_required(login_url='/accounts/login/')
def comunicado_detalhe(request, pk):
    comunicado = Comunicados.objects.get(pk=pk)
    context = {
        'comunicado':comunicado,
    }
    return render(request, 'Atividades/comunicado_detalhe.html', context)

@login_required(login_url='/accounts/login/')
def comunicados(request):
    try:
        comunicados = Comunicados.objects.all().order_by('-data')
    except:
        comunicados = None

    paginator = Paginator(comunicados, 50)

    # Esteja certo de que o `page request` é um inteiro. Se não, mostre a primeira página.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        comunicados = paginator.page(page)
    except (EmptyPage, InvalidPage):
        comunicados = paginator.page(paginator.num_pages)

    var_get_search = request.POST.get('search_box')


    if var_get_search is not None:
        comunicados = comunicados.filter(Q(tipo__icontains=var_get_search)
            | Q(servidor__username__icontains=var_get_search)
            | Q(aluno__nome__icontains=var_get_search)
        )

    context = {'comunicados':comunicados}

    return render(request, 'Atividades/comunicado_lista.html', context)


def acesso_msg(request):
    """ Mensagem para usuario nao autenticado """
    return render(request, 'Atividades/acesso_negado.html')


def header(canvas, doc):
    # Save the state of our canvas so we can draw on it
    canvas.saveState()
    canvas.setFont("Times-Roman", 12)
    left = 0.98*inch
    right = 600-0.59*inch
    y = 731
    canvas.setTitle("documento_oficial_webCGAE")
    fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/Atividades/icon_ifc2.jpg')
    canvas.drawImage(fn, 10.2*cm, 770, width=40,height=40)
    canvas.drawCentredString(11.0*cm,760, "Ministério da Educação")
    canvas.drawCentredString(11.0*cm,747, "Secretaria de Educação Profissional e Tecnológica")
    canvas.drawCentredString(11.0*cm,735, "Instituto Federal Catarinense")
    canvas.line(left,y, right,y)

    canvas.setFont("Times-Roman", 10)
    canvas.line(left, y-24.4*cm, right, y-24.4*cm)
    fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/Atividades/icon_ifc.png')
    canvas.drawImage(fn, left+10, y-25.7*cm, width=140,height=35)
    canvas.drawRightString(550, y-24.8*cm, "Rua das Missões, 100 - Ponta Aguda" )
    canvas.drawRightString(550, y-25.2*cm, "Blumenau/SC - CEP: 89.051-000" )
    canvas.drawRightString(550, y-25.6*cm, "(47) 3331-7800 / ifc@ifc.edu.br" )


    # Release the canvas
    canvas.restoreState()


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Times-Roman", 10)
    left = 0.98*inch
    right = 600-0.59*inch
    y = 731
    canvas.line(left, y-24.4*cm, right, y-24.4*cm)
    fn = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static/Atividades/icon_ifc.png')
    canvas.drawImage(fn, left+10, y-25.7*cm, width=140,height=35)
    canvas.drawRightString(550, y-24.8*cm, "Rua das Missões, 100 - Ponta Aguda" )
    canvas.drawRightString(550, y-25.2*cm, "Blumenau/SC - CEP: 89.051-000" )
    canvas.drawRightString(550, y-25.6*cm, "(47) 3331-7800 / ifc@ifc.edu.br" )

    canvas.restoreState()


def gerar_pdf_denuncia(request, pk):
    relatorio = Relatorio.objects.get(pk=pk)

    if not relatorio.denuncia:

        doc = SimpleDocTemplate('/tmp/denuncia.pdf',
                                pagesize=A4,
                                rightMargin=1.5*cm,
                                leftMargin=2.5*cm,
                                topMargin=1.3*cm,
                                bottomMargin=1.27*cm)


        Story = []
        styles = {
            'default': ParagraphStyle(
                    'default',
                    fontName='Times-Roman',
                    fontSize=12,
                    firstLineIndent=70.8,
                    leading=18,
                    alignment=TA_JUSTIFY,
                    ),
        }

        styles['titulo'] = ParagraphStyle(
                'titulo',
                parent=styles['default'],
                firstLineIndent=0,
                fontName='Times-Bold',
                fontSize=12,
                alignment=TA_CENTER,
        )
        styles['data'] = ParagraphStyle(
                'data',
                parent=styles['default'],
                firstLineIndent=0,
                fontName='Times-Roman',
                fontSize=12,
                alignment=TA_CENTER,
        )
        styles['assign'] = ParagraphStyle(
                'assign',
                parent=styles['default'],
                firstLineIndent=0,
                fontName='Times-Italic',
                fontSize=12,
                alignment=TA_CENTER,
        )
        styles['final'] = ParagraphStyle(
                'final',
                parent = styles['default'],
                firstLineIndent=0,
                fontName = 'Times-Roman',
                alignment=TA_JUSTIFY,
        )


        texto_titulo = 'COMUNICAÇÃO DE DENÚNCIA'

        if relatorio.artigo > "Art.20":
            tipo_ato = "infração exposta"
        else:
            tipo_ato = "ato de indisciplina exposto"

        txt1 = 'Nome do(a) denunciante: %s'%relatorio.denunciante
        txt2 = 'Nome do(a) denunciado(a): %s'%relatorio.denunciado



        txt4 = 'DENÚNCIA'
        txt5 = relatorio.texto

        #verifica qual o enquadramento legal
        aux = relatorio.artigo.split("-")
        if aux[0] == 'Art.18':
            if aux[1] == 'I':
                txt_regulamento = REGULAMENTO[0]
            elif aux[1] == "II":
                txt_regulamento = REGULAMENTO[1]
            elif aux[1] == "III":
                txt_regulamento = REGULAMENTO[2]
            elif aux[1] == "IV":
                txt_regulamento = REGULAMENTO[3]
            elif aux[1] == "V":
                txt_regulamento = REGULAMENTO[4]
            elif aux[1] == "VI":
                txt_regulamento = REGULAMENTO[5]
            elif aux[1] == "VII":
                txt_regulamento = REGULAMENTO[6]
            elif aux[1] == "VIII":
                txt_regulamento = REGULAMENTO[7]
            elif aux[1] == "IX":
                txt_regulamento = REGULAMENTO[8]
            elif aux[1] == "X":
                txt_regulamento = REGULAMENTO[9]
            elif aux[1] == "XI":
                txt_regulamento = REGULAMENTO[10]
        elif aux[0] == 'Art.19':
            if aux[1] == 'I':
                txt_regulamento = REGULAMENTO[11]
            elif aux[1] == 'II':
                txt_regulamento = REGULAMENTO[12]
            elif aux[1] == 'III':
                txt_regulamento = REGULAMENTO[13]
            elif aux[1] == 'IV':
                txt_regulamento = REGULAMENTO[14]
            elif aux[1] == 'V':
                txt_regulamento = REGULAMENTO[15]
            elif aux[1] == 'VI':
                txt_regulamento = REGULAMENTO[16]
            elif aux[1] == 'VII':
                txt_regulamento = REGULAMENTO[17]
            elif aux[1] == 'VIII':
                txt_regulamento = REGULAMENTO[18]
            elif aux[1] == 'IX':
                txt_regulamento = REGULAMENTO[19]
            elif aux[1] == 'X':
                txt_regulamento = REGULAMENTO[20]
            elif aux[1] == 'XI':
                txt_regulamento = REGULAMENTO[21]
            elif aux[1] == 'XII':
                txt_regulamento = REGULAMENTO[22]
            elif aux[1] == 'XIII':
                txt_regulamento = REGULAMENTO[23]
            elif aux[1] == 'XIV':
                txt_regulamento = REGULAMENTO[24]
        elif aux[0] == 'Art.20':
            if aux[1] == 'I':
                txt_regulamento = REGULAMENTO[25]
            elif aux[1] == 'II':
                txt_regulamento = REGULAMENTO[26]
            elif aux[1] == 'III':
                txt_regulamento = REGULAMENTO[27]
            elif aux[1] == 'IV':
                txt_regulamento = REGULAMENTO[28]
            elif aux[1] == 'V':
                txt_regulamento = REGULAMENTO[29]
        elif aux[0] == 'Art.21':
            if aux[1] == 'I':
                txt_regulamento = REGULAMENTO[30]
            elif aux[1] == 'II':
                txt_regulamento = REGULAMENTO[31]
            elif aux[1] == 'III':
                txt_regulamento = REGULAMENTO[32]
            elif aux[1] == 'IV':
                txt_regulamento = REGULAMENTO[33]
            elif aux[1] == 'V':
                txt_regulamento = REGULAMENTO[34]
            elif aux[1] == 'VI':
                txt_regulamento = REGULAMENTO[35]
            elif aux[1] == 'VII':
                txt_regulamento = REGULAMENTO[36]
            elif aux[1] == 'VIII':
                txt_regulamento = REGULAMENTO[37]
            elif aux[1] == 'IX':
                txt_regulamento = REGULAMENTO[38]
            elif aux[1] == 'X':
                txt_regulamento = REGULAMENTO[39]
            elif aux[1] == 'XI':
                txt_regulamento = REGULAMENTO[40]
            elif aux[1] == 'XII':
                txt_regulamento = REGULAMENTO[41]
            elif aux[1] == 'XIII':
                txt_regulamento = REGULAMENTO[42]
            elif aux[1] == 'XIV':
                txt_regulamento = REGULAMENTO[43]
            elif aux[1] == 'XV':
                txt_regulamento = REGULAMENTO[44]
            elif aux[1] == 'XVI':
                txt_regulamento = REGULAMENTO[45]
            elif aux[1] == 'XVII':
                txt_regulamento = REGULAMENTO[46]
            elif aux[1] == 'XVIII':
                txt_regulamento = REGULAMENTO[47]
            elif aux[1] == 'XIX':
                txt_regulamento = REGULAMENTO[48]
            elif aux[1] == 'XX':
                txt_regulamento = REGULAMENTO[49]
            elif aux[1] == 'XXI':
                txt_regulamento = REGULAMENTO[50]
            elif aux[1] == 'XXII':
                txt_regulamento = REGULAMENTO[51]
            elif aux[1] == 'XXIII':
                txt_regulamento = REGULAMENTO[52]
            elif aux[1] == 'XXIV':
                txt_regulamento = REGULAMENTO[53]
            elif aux[1] == 'XXV':
                txt_regulamento = REGULAMENTO[54]
            elif aux[1] == 'XXVI':
                txt_regulamento = REGULAMENTO[55]
            elif aux[1] == 'XXVII':
                txt_regulamento = REGULAMENTO[56]
            elif aux[1] == 'XXVIII':
                txt_regulamento = REGULAMENTO[57]
            elif aux[1] == 'XXIX':
                txt_regulamento = REGULAMENTO[58]
            elif aux[1] == 'XXX':
                txt_regulamento = REGULAMENTO[59]
            elif aux[1] == 'XXXI':
                txt_regulamento = REGULAMENTO[60]
            elif aux[1] == 'XXXII':
                txt_regulamento = REGULAMENTO[61]
            elif aux[1] == 'XXXIII':
                txt_regulamento = REGULAMENTO[62]
            elif aux[1] == 'XXXIV':
                txt_regulamento = REGULAMENTO[63]


        txt6 = 'Diante dos fatos narrados, verifica-se que o conteúdo da \
                denúncia refere-se a %s \
                no %s, do Regulamento de Conduta Discente.\
                A denúncia será encaminhada para apuração pelos órgãos\
                competentes.'%(tipo_ato, txt_regulamento )

        hj = date.today()
        txt7 = 'Rio do Sul /SC, %s de %s de %s.'%(hj.day, MESES[hj.month-1], hj.year)

        txt8 = str(relatorio.servidor.get_full_name())
        txt9 = "Denunciante"

        Story.append(Spacer(1, 100))
        Story.append(Paragraph(texto_titulo, styles['titulo']))
        Story.append(Spacer(1,60))
        Story.append(Paragraph(txt1, styles['final']))
        Story.append(Spacer(1,30))
        Story.append(Paragraph(txt2, styles['final']))
        Story.append(Spacer(1,30))
        Story.append(Paragraph(txt4, styles['data']))
        Story.append(Spacer(1,30))
        Story.append(Paragraph(txt5, styles['default']))
        Story.append(Paragraph(txt6, styles['default']))
        Story.append(Spacer(1,40))
        Story.append(Paragraph(txt7, styles['data']))
        Story.append(Spacer(1,40))

        #relator
        d = Drawing(100,1)
        d.add(Line(120, 0, 350, 0))
        Story.append(d)
        Story.append(Spacer(1,5))
        Story.append(Paragraph(txt8, styles['data']))

        #denunciante
        Story.append(Spacer(1,40))
        d = Drawing(100,1)
        d.add(Line(120, 0, 350, 0))
        Story.append(d)
        Story.append(Spacer(1,5))
        Story.append(Paragraph(txt9, styles['data']))


        doc.build(Story, onFirstPage=header, onLaterPages=footer)

        relatorio.denuncia = True
        relatorio.save()

        fs = FileSystemStorage("/tmp")
        with fs.open("denuncia.pdf") as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="denuncia.pdf"'
            return response

        return response


    else:
        return redirect('relatorio_detalhe', relatorio.id)


def gerar_pdf_comunicacao(request, pk):
    relatorio = Relatorio.objects.get(pk=pk)

    if  not relatorio.comunicado_discente:
        aluno = Aluno.objects.get(matricula=relatorio.denunciado.matricula)
        try:
            perfil = Perfil.objects.get(aluno=relatorio.denunciado)
        except:
            perfil = None
        try:
            dados = Curso.objects.get(aluno=relatorio.denunciado)
        except:
            dados = None


        doc = SimpleDocTemplate('/tmp/comunicacao_discente.pdf',
                                pagesize=A4,
                                rightMargin=1.5*cm,
                                leftMargin=2.5*cm,
                                topMargin=1.3*cm,
                                bottomMargin=1.27*cm)

        Story = []
        styles = {
            'default': ParagraphStyle(
                    'default',
                    fontName='Times-Roman',
                    fontSize=11,
                    firstLineIndent=70.8,
                    leading=18,
                    alignment=TA_JUSTIFY,
                    ),
        }

        styles['titulo'] = ParagraphStyle(
                'titulo',
                parent=styles['default'],
                firstLineIndent=0,
                fontName='Times-Bold',
                fontSize=11,
                alignment=TA_CENTER,
        )
        styles['data'] = ParagraphStyle(
                'data',
                parent=styles['default'],
                firstLineIndent=0,
                fontName='Times-Roman',
                fontSize=11,
                alignment=TA_CENTER,
        )
        styles['assign'] = ParagraphStyle(
                'assign',
                parent=styles['default'],
                firstLineIndent=0,
                fontName='Times-Italic',
                fontSize=11,
                alignment=TA_CENTER,
        )
        styles['final'] = ParagraphStyle(
                'final',
                parent = styles['default'],
                firstLineIndent=0,
                fontName = 'Times-Roman',
                alignment=TA_JUSTIFY,
        )
        styles['discente'] = ParagraphStyle(
                'discente',
                parent  = styles['default'],
                firstLineIndent=70,
        )
        styles['responsavel'] = ParagraphStyle(
                'responsavel',
                parent  = styles['default'],
                firstLineIndent=50,
        )

        texto_titulo = "COMUNICAÇÃO AO(À) DISCENTE"



        texto1 = '<font size=11>Ao(À) discente %s, matriculado(a) no IFC - \
        Campus Rio do Sul, sob número de matrícula %d, turma %s.</font>'%(relatorio.denunciado,
                                                                          aluno.matricula,
                                                                          aluno.turma)


        if relatorio.artigo > "Art.20":
            tipo_ato = "infração"
        else:
            tipo_ato = "ato de indisciplina"

        title = "a "
        titulo = relatorio.titulo
        titulo = titulo.lower()
        title += titulo



        texto2 = '<font size=11> Olavo Acácio Paulik, Coordenador do CGAE, \
        tendo em vista a aplicação do Regulamento de Conduta Discente, COMUNICA \
        que, no dia %s de %s de %s, foi recebida denúncia de %s, referente %s,\
        previsto(a) no %s, do Regulamento de Conduta Discente, no qual seu nome \
        figura na condição de denunciado(a). Essa denúncia será apurada, e seu\
        direito à ampla defesa e ao contraditório serão garantidos em momento\
        oportuno, em relação ao qual será previamente comunicado(a).</font>'%(relatorio.data.day,
                                                                              MESES[relatorio.data.month-1],
                                                                              relatorio.data.year,
                                                                              tipo_ato,
                                                                              title,
                                                                              relatorio.artigo,
                                                                              )


        texto3 = '<font size=11>Os atos  serão realizados nas dependências do \
        Campus Rio do Sul, do IFC, onde lhe será facultada vista dos autos ou \
        dos trabalhos, sendo o discente e/ou responsáveis comunicados sobre\
        as datas dos mesmos oportunamente.</font>'

        hj = date.today()
        texto4 = '<font size=11>Rio do Sul/SC, %s de %s de %s</font>'%(hj.day, MESES[hj.month], hj.year)

        texto5 = '<font size=11>Coordenador(a) do CAE/CGAE </font>'

        texto6 = '<font size=11>Em ______/_______/ de __________ . Recebi: Cópia do registro da denúncia anexa.</font>'

        text7 = '<font size=11>Discente</font>'
        texto8 = '<font size=11>Responsável legal</font>'

        Story.append(Spacer(1,100))
        Story.append(Paragraph(texto_titulo, styles["titulo"]))
        Story.append(Spacer(1,50))
        Story.append(Paragraph(texto1, styles["default"]))
        Story.append(Paragraph(texto2, styles["default"]))
        Story.append(Paragraph(texto3, styles["default"]))
        Story.append(Spacer(1,20))
        Story.append(Paragraph(texto4, styles['data']))
        Story.append(Spacer(1,50))

        d = Drawing(100, 1)
        d.add(Line(120, 0, 350, 0))
        Story.append(d)
        Story.append(Spacer(1,8))
        Story.append(Paragraph(texto5, styles['assign']))
        Story.append(Spacer(1,20))
        Story.append(Paragraph(texto6, styles['final']))
        Story.append(Spacer(1,50))

        b = Drawing(100,1)
        b.add(Line(20, 0, 160, 0))
        Story.append(b)
        Story.append(Spacer(1,8))
        Story.append(Paragraph(text7, styles['discente']))

        Story.append(Spacer(1,50))
        c = Drawing(100,1)
        c.add(Line(20, 0, 160, 0))
        Story.append(c)
        Story.append(Spacer(1,8))
        Story.append(Paragraph(texto8, styles['responsavel']))


        doc.build(Story, onFirstPage=header, onLaterPages=footer)

        relatorio.comunicado_discente = True
        relatorio.save()

        fs = FileSystemStorage("/tmp")
        with fs.open("comunicacao_discente.pdf") as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="comunicao_discente.pdf"'
            return response

        return response

    else:
        return redirect('relatorio_detalhe', relatorio.id)


def gerar_pdf_comunicado(request, pk):
    comunicado = Comunicados.objects.get(pk=pk)
    doc = SimpleDocTemplate('/tmp/comunicado_pais.pdf',
                            pagesize=A4,
                            rightMargin=1.5*cm,
                            leftMargin=2.5*cm,
                            topMargin=1.3*cm,
                            bottomMargin=1.27*cm)

    Story = []
    styles = {
        'default': ParagraphStyle(
                'default',
                fontName='Times-Roman',
                fontSize=12,
                firstLineIndent=70.8,
                leading=18,
                alignment=TA_JUSTIFY,
                ),
    }
    styles['titulo'] = ParagraphStyle(
            'titulo',
            parent=styles['default'],
            firstLineIndent=0,
            fontName='Times-Bold',
            fontSize=12,
            alignment=TA_CENTER,
    )
    styles['ciente'] = ParagraphStyle(
            'ciente',
            parent=styles['default'],
            firstLineIndent=0,
    )
    styles['assign'] = ParagraphStyle(
            'assign',
            parent=styles['default'],
            firstLineIndent=0,
            alignment=TA_CENTER,
    )
    styles['data'] = ParagraphStyle(
            'data',
            parent=styles['default'],
            firstLineIndent=0,
            alignment=TA_RIGHT,
    )

    texto_titulo = "COMUNICADO"
    texto_subtitulo = "Discente: %s"% str(comunicado.aluno)

    hj = date.today()
    texto_recebido = "Recebido em ______/______/ %s."%hj.year
    texto_data = 'Rio do Sul, %s de %s de %s.'%(hj.day, MESES[hj.month], hj.year)
    texto_comunicado = comunicado.texto

    texto_ciente = 'Eu, ________________________________________________, \
                    responsável pelo (a) estudante %s, estou ciente do \
                    acontecimento envolvendo meu filho(a).'%str(comunicado.aluno)

    texto_assign_escola = "%s"%(str(comunicado.servidor.get_full_name()))

    texto_assign_pais = "Responsável legal"


    Story.append(Spacer(1,100))
    Story.append(Paragraph(texto_titulo, styles["titulo"]))
    Story.append(Spacer(1,25))
    Story.append(Paragraph(texto_data, styles['data']))
    Story.append(Spacer(1,25))
    Story.append(Paragraph(texto_subtitulo, styles["default"]))
    Story.append(Spacer(1,50))
    Story.append(Paragraph(texto_comunicado, styles["default"]))
    Story.append(Spacer(1,20))
    Story.append(Paragraph(texto_ciente, styles['ciente']))
    Story.append(Spacer(1,70))

    d = Drawing(100, 1)
    d.add(Line(120, 0, 350, 0))
    Story.append(d)
    Story.append(Spacer(1,8))
    Story.append(Paragraph(texto_assign_escola, styles['assign']))
    Story.append(Spacer(1,50))
    Story.append(Paragraph(texto_recebido, styles['ciente']))
    Story.append(Spacer(1,70))

    d = Drawing(100, 1)
    d.add(Line(120, 0, 350, 0))
    Story.append(d)
    Story.append(Spacer(1,8))
    Story.append(Paragraph(texto_assign_pais, styles['assign']))


    doc.build(Story, onFirstPage=header, onLaterPages=footer)

    fs = FileSystemStorage("/tmp")
    with fs.open("comunicado_pais.pdf") as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="comunicado_pais.pdf"'
        return response

    return response
