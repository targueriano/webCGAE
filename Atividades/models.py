# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from Pessoas.models import Aluno
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse

# Create your models here.
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Create your models here.

class Relatorio(models.Model):

    CONDUTA = (
        ('Ato de indisciplina de baixa gravidade',
            (
                (u'Art.18-I', u"""Art.18, I Faltar com asseio pessoal e organização
                dos seus pertences e dos recursos e/ou equipamentos do IFC sob sua
                responsabilidade ou uso."""),
                (u'Art.18-II', u"""Art.18, II
                Descumprir o horário geral das atividades do campus."""),
                (u'Art.18-III', u"""Art.18, III
                Proferir palavras obscenas ou ofensivas."""),
                (u'Art.18-IV', u"""Art.18, IV Fazer gestos obscenos."""),
                (u'Art.18-V', u"""Art.18, V Não cumprir as escalas de atividades
                pedagógicas curriculares optativas."""),
                (u'Art.18-VI', u"""Art.18, VI Descumprir as normas do campus que
                orientam o uso de instalações e serviços"""),
                (u'Art.18-VII', u"""Art.18, VII Manter-se em
                atitude de desinteresse ou com vistas à desordem das atividaes pedagógicas."""),
                (u'Art.18-VIII', u"""Art.18, VIII Incumbir outra pessoa do desempenho
                de tarefa que seja de sua responsabilidade."""),
                (u'Art.18-IX', u"""Art.18, IX Apresentar-se sem uniforme nas atividades
                pedagógicas, caso as normas estabelecidas pelo campus instituam a necessidade
                de seu uso."""),
                (u'Art.18-X', u"""Art.18, X Entrar nas dependências do IFC sem autorização
                ou identificação, caso as normas estabelecidas pelo campus instituam essa
                necessidade."""),
                (u'Art.18-XI', u"""Art.18, XI Ter outros comportamentos, não constantes
                nesse rol, que podem ser equiparados, pelo CAE/CGAE do campus ou pela
                coordenação de curso, aos atos aqui arrolados.(REVOGADO)"""),
            )
        ),
        ('Ato de indisciplina de média gravidade',
            (
                (u'Art.19-I', u"""Art.19, I Ausentar-se da sala de aula ou das dependências do IFC
                sem autorização, caso as normas estabelecidas pelo campus instituam essa
                necessidade."""),
                (u'Art.19-II', u"""Art.19, II Omitir-se, sem justificativa, de programações
                esportivas, cívicas, artísticas e culturais, e viagens acadêmicas
                quando estiver representando o campus dentro ou fora do IFC."""),
                (u'Art.19-III', u"""Art.19, III Descumprir as tarefas pedagógicas,
                sem justificativas previstas em lei."""),
                (u'Art.19-IV', u"""Art.19, IV Usar de meios ilícitos durante
                realização de atividades avaliativas."""),
                (u'Art.19-V', u"""Art.19, V Usar
                de desonestidade para eximir-se das atividades pedagógicas."""),
                (u'Art.19-VI', u"""Art.19, VI Omitir
                ou distorcer informações quando solicitadas."""),
                (u'Art.19-VII', u"""Art.19, VII Utilizar o telefone celular ou outro equipamento
                eletrônico que interfira no bom andamento das atividades pedagógicas, salvo
                os casos [...] autorizados [...]."""),
                (u'Art.19-VIII', u"""Art.19, VIII Efetuar transação comercial, inclusive
                rifas e sorteios, dentro do campus, sem a devida autorização."""),
                (u'Art.19-IX', u"""Art.19, IX Apresentar comportamentos ou vestimentas
                que atentem ao pudor."""),
                (u'Art.19-X', u"""Art.19, X Fazer uso indevido de recursos tecnológicos
                (redes sociais, mensagens instantâneas, sites em geral, e-mail, entr outros),
                de forma a infringir o presente Regulamento."""),
                (u'Art.19-XI', u"""Art.19, XI Negligenciar o cuidado com  os animais sob sua
                responsabilidade."""),
                (u'Art.19-XII', u"""Art.19, XII Adentrar e permanecer, em sala de aula
                e/ou outros locais fechados, nas dependências do IFC, com animais[...]."""),
                (u'Art.19-XIII', u"""Art.19, XIII Adentrar e permanecer nos locais
                de atividades pedagógicas com pessoas não-matriculadas, sem autorização
                prévia do(a) docente ou coordenador(a) responsável."""),
                (u'Art.19-XIV', u"""Art.19, XIV Ter outros comportamentos, não constantes
                nesse rol, que podem ser equiparados, pelo CAE/CGAE do campus ou pela
                coordenação de curso, aos atos aqui arrolados.(REVOGADO)"""),
            )
        ),
        ('Ato de indisciplina de alta gravidade',
            (
                (u'Art.20-I', u"""Art.20, I Usar barragens, rios, lagos e açudes, do campus
                e proximidades, para banho, pesca ou outras atividades afins sem autorização."""),
                (u'Art.20-II', u"""Art.20, II Recusar-se a seguir as normas de segurança do trabalho
                nas aulas de laboratório, e/ou de campo, e visitas técnicas."""),
                (u'Art.20-III', u"""Art.20, III Organizar e/ou praticar trote em discentes
                sem a autorização da Coordenação do curso."""),
                (u'Art.20-IV', u"""Art.20, IV Portar ou depositar bebida alcoólica, cigarros ou
                outras drogras lícitas, nas dependências do IFC, se maior de idade."""),
                (u'Art.20-V', u"""Art.20, V Ter outros comportamentos, não constantes
                nesse rol, que podem ser equiparados, pelo CAE/CGAE do campus ou pela
                coordenação de curso, aos atos aqui arrolados.(REVOGADO)"""),
            )
        ),
        ('Infrações',
            (
                (u'Art.21-I', u"""Art.21, I Coagir outra pessoa a qualquer atitude
                 contrária a sua vontade."""),
                (u'Art.21-II', u"""Art.21, II Coagir membro da comunidade do IFC
                ou qualquer visitante à prática de atos atentatórios à Lei."""),
                (u'Art.21-III', u"""Art.21, III Furtar, ou sua tentativa."""),
                (u'Art.21-IV', u"""Art.21, IV Roubar, ou sua tentativa."""),
                (u'Art.21-V', u"""Art.21, V Portar ou usar qualquer espécie de arma."""),
                (u'Art.21-VI', u"""Art.21, VI Tentar agredir ou agredir física e/ou
                 moralmente qualquer pessoa, nas depências do IFC ou em âmbito
                 externo, quando em atividades pedagógicas ou em representação
                 do IFC."""),
                (u'Art.21-VII', u"""Art.21, VII Expor, intencionalmente ou não,
                a perigo a vida ou saúde de outrem."""),
                (u'Art.21-VIII', u"""Art.21, VIII Praticar atos libidinosos ou obscenos."""),
                (u'Art.21-IX', u"""Art.21, IX Ameaçar alguém oralmente, por escrito,
                por meio de gestos ou qualquer outro meio simbólico."""),
                (u'Art.21-X', u"""Art.21, X Deixar de prestar assistência à pessoa
                ameaçada, constrangida ou exposta a iminente perigo, ou, quando
                não for possível fazê-lo sem risco à própria integridade física, não
                solicitar o socorro devido."""),
                (u'Art.21-XI', u"""Art.21, XI Usar de maneira indevida os diferentes espaços
                do campus, colocando em risco a integridade própria e/ou de
                terceiros."""),
                (u'Art.21-XII', u"""Art.21, XII Praticar atos atentatórios
                à dignidade [...]."""),
                (u'Art.21-XIII', u"""Art.21, XIII Aplicar trotes atentatórios
                à dignidade ou que coloquem em risco à vida de outrem."""),
                (u'Art.21-XIV', u"""Art.21, XIV Praticar, induzir ou incitar,
                por qualquer meio, a discriminação ou o preconceito [...]."""),
                (u'Art.21-XV', u"""Art.21, XV Praticar toda e qualquer ação de
                intimidação, agressões intencionais, verbais ou físicas feitas
                de maneira repetitiva, que configure a prática de bullying."""),
                (u'Art.21-XVI', u"""Art.21, XVI Praticar violência ou abuso
                contra animais, ou qualquer outra forma de violação das leis vigentes."""),
                (u'Art.21-XVII', u"""Art.21, XVII Portar ou depositar bebida alcoólica,
                cigarros ou outras drogas lícitas, nas dependências do IFC, se menor de idade."""),
                (u'Art.21-XVIII', u"""Art.21, XVIII Portar ou depositar drogas
                ilícitas nas dependências do IFC."""),
                (u'Art.21-XIX', u"""Art.21, XIX Usar ou incentivar o uso de
                drogas lícitas e ilícitas, ou apresentar sintomas de seu
                uso, nas dependências do IFC ou externamente, em atividades
                executadas pelo IFC, de que o (a) discente faça parte."""),
                (u'Art.21-XX', u"""Art.21, XX Comercializar, fornecer, servir,
                 ministrar ou entregar bebida alcoólica, cigarro ou outras
                 drogas lícitas e ilícitas, dentro do IFC, em atividade
                 pedagógica ou atividade em que estiver representando o IFC."""),
                (u'Art.21-XXI', u"""Art.21, XXI Adulterar ou falsificar pareceres
                ou documentos."""),
                (u'Art.21-XXII', u"""Art.21, XXII Recorrer a meios fraudulentos para lograr
                vantagem para si ou para outrem."""),
                (u'Art.21-XXIII', u"""Art.21, XXIII Utilizar pessoal ou recursos
                materiais do IFC em serviços ou atividades particulares."""),
                (u'Art.21-XXIV', u"""Art.21, XXIV Depredar o patrimônio público
                ou privado."""),
                (u'Art.21-XXV', u"""Art.21, XXV Promover ou participar de atos de
                vandalismo."""),
                (u'Art.21-XXVI', u"""Art.21, XXVI Praticar a retirada de equipamentos,
                produtos e outros itens que constituem patrimônio do IFC,
                sem a prévia autorização de seus responsáveis."""),
                (u'Art.21-XXVII', u"""Art.21, XXVII Cometer plágio, ou seja,
                apropriar-se, parcialmente ou na íntegra, do trabalho de outrem
                e utilizá-lo como se fosse seu, sem lhe dar o devido crédito,
                ou seja, sem citá-lo como fonte."""),
                (u'Art.21-XXVIII', u"""Art.21, XXVIII Usar de forma indevida o
                nome ou o símbolo do IFC, sendo agravante o uso a fim de
                tirar proveito, para si ou para outrem, ou a fim de difamar a instituição."""),
                (u'Art.21-XXIX', u"""Art.21, XXIX Promover eventos usando o
                nome do IFC sem a devida autorização da Direção."""),
                (u'Art.21-XXX', u"""Art.21, XXX  Divulgar, ceder ou comercializar
                dados relativos a pesquisas do IFC, sem a autorização de
                autoridade competente."""),
                (u'Art.21-XXXI', u"""Art.21, XXXI Devassar o conteúdo ou se
                apossar indevidamente de correspondência alheia."""),
                (u'Art.21-XXXII', u"""Art.21, XXXII Acessar computadores, softwares,
                dados, informações, redes ou porções restritas do sistema
                computacional do IFC, sem a devida autorização."""),
                (u'Art.21-XXXIII', u"""Art.21, XXXIII Enviar spams, mensagens
                fraudulentas, pornográficas ou ameaçadoras."""),
                (u'Art.21-XXXIV', u"""Art.21, XXXIV Outros, não constantes
                neste rol, que se caracterizem como infrações.(REVOGADO)"""),
            )
        ),
    )

    MEDIDA = (
        (u'Advertência escrita', u'Advertência escrita (baixa ou média gravidade)'),
        (u'Realização de atividades pedagógicas específicas', u"""Realização de atividades pedagógicas específicas
        (baixa, média, alta gravidade ou infrações)"""),
        (u'Reparação do dano causado ao patrimônio\
        público ou particular', u"""Reparação do dano causado ao patrimônio
        público ou particular (Alta gravidade ou infrações)"""),
        (u'Retratação verbal ou escrita', u'Retratação verbal ou escrita (baixa, média, alta gravidade ou infrações)'),
        (u"""Suspensão da frequência às atividades curriculares""", u"""Suspensão da frequência às atividades curriculares
        obrigatórias e/ou optativas, acompanhada da realização de atividades
         pedagógicas específicas (Alta gravidade ou infrações)"""),
        (u'Mudança de turno ou turma', u'Mudança de turno ou turma (Alta gravidade ou infrações)'),
        (u"""Transferência compulsória, se discente do ensino médio""", u"""Transferência
        compulsória, se discente do ensino médio (Infrações)"""),
        (u"""Desligamento ou não-renovação da matrícula, se
        discente de ensino superior""", u"""Desligamento ou não-renovação da matrícula, se
        discente de ensino superior (Infrações)"""),
    )
    #index = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=150, help_text="Palavras-chave para resumir o evento.")
    denunciante = models.CharField(max_length=100,
    blank=True, null=True, help_text="Aluno ou Servidor")
    denunciado = models.ForeignKey(Aluno)
    artigo = models.CharField(choices=CONDUTA,
                              max_length=300,
                              null=False,
                              blank=False,
                              )

    medida_prevista = models.CharField(choices=MEDIDA,
                                       max_length=250,
                                       null=False,
                                       blank=False)

    texto = models.TextField(max_length=100000, help_text='Os fatos ocorridos.')
    data = models.DateField()
    servidor = models.ForeignKey(User, help_text='Servidor que está elaborando a denúncia.')
    denuncia = models.BooleanField('Escrito denúncia', default=False)
    comunicado_discente = models.BooleanField('Comunicado ao discente', default=False)
    encaminhado_conciliacao = models.BooleanField('Encaminhado para conciliação', default=False)
    protocolado = models.BooleanField('Protocolado', default=False)
    medida_aplicada = models.BooleanField(default=False, editable=True)
    tipo_medida = models.CharField('Tipo de medida',choices=MEDIDA, max_length=250, null=True, blank=True)
    controle = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return str(self.denunciado)


    def get_absolute_url(self):
        return reverse('relatorio_lista',)

    class Meta:
        ordering = ['data']
        verbose_name = "Relatório"
        verbose_name_plural = "Relatórios"


class Vistoria(models.Model):
    ALOJA = (
        (u'1A', u'1A'),
        (u'1B', u'1B'),
        (u'1C', u'1C'),
        (u'1D', u'1D'),
        (u'1E', u'1E'),
        (u'1F', u'1F'),
        (u'2A', u'2A'),
        (u'2B', u'2B'),
        (u'2C', u'2C'),
        (u'2D', u'2D'),
        (u'2E', u'2E'),
        (u'1F', u'2F'),
        (u'3A', u'3A'),
        (u'3B', u'3B'),
        (u'3C', u'3C'),
        (u'3D', u'3D'),
        (u'3E', u'3E'),
        (u'3F', u'3F'),
        (u'4A', u'4A'),
        (u'4B', u'4B'),
        (u'4C', u'4C'),
        (u'4D', u'4D'),
        (u'4E', u'4E'),
        (u'4F', u'4F'),
        (u'5A', u'5A'),
        (u'5B', u'5B'),
        (u'5C', u'5C'),
        (u'5D', u'5D'),
        (u'5E', u'5E'),
        (u'5F', u'5F'),
        (u'6A', u'6A'),
        (u'6B', u'6B'),
        (u'6C', u'6C'),
        (u'6D', u'6D'),
        (u'6E', u'6E'),
        (u'6F', u'6F'),
        (u'7A', u'7A'),
        (u'7B', u'7B'),
        (u'7C', u'7C'),
        (u'7D', u'7D'),
        (u'7E', u'7E'),
        (u'1F', u'7F'),
        (u'8A', u'8A'),
        (u'8B', u'8B'),
        (u'8C', u'8C'),
        (u'8D', u'8D'),
        (u'8E', u'8E'),
        (u'8F', u'8F'),
        (u'9A', u'9A'),
        (u'9B', u'9B'),
        (u'9C', u'9C'),
        (u'9D', u'9D'),
        (u'9E', u'9E'),
        (u'9F', u'9F'),
        (u'10A', u'10A'),
        (u'10B', u'10B'),
        (u'10C', u'10C'),
        (u'10D', u'10D'),
        (u'10E', u'10E'),
        (u'10F', u'10F'),
        (u'11A', u'11A'),
        (u'11B', u'11B'),
        (u'11C', u'11C'),
        (u'11D', u'11D'),
        (u'11E', u'11E'),
        (u'11F', u'11F'),
        (u'12A', u'12A'),
        (u'12B', u'12B'),
        (u'12C', u'12C'),
        (u'12D', u'12D'),
        (u'12E', u'12E'),
        (u'12F', u'12F'),
        (u'13A', u'13A'),
        (u'13B', u'13B'),
        (u'13C', u'13C'),
        (u'13D', u'13D'),
        (u'13E', u'13E'),
        (u'13F', u'13F'),
        (u'14A', u'14A'),
        (u'14B', u'14B'),
        (u'14C', u'14C'),
        (u'14D', u'14D'),
        (u'14E', u'14E'),
        (u'14F', u'14F'),
        (u'15A', u'15A'),
        (u'15B', u'15B'),
        (u'15C', u'15C'),
        (u'15D', u'15D'),
        (u'15E', u'15E'),
        (u'15F', u'15F'),
    )
    NIVEL = (
        (u'Muito ruim', u'Muito ruim'),
        (u'Ruim', u'Ruim'),
        (u'Regular', u'Regular'),
        (u'Bom', u'Bom'),
        (u'Ótimo', u'Ótimo'),
    )
    MOTIVOS = (
        (u'Pedido de troca', u'Pedido de troca'),
        (u'Interesse da administração', u'Interesse da administração'),
    )
    quarto = models.CharField(choices=ALOJA, max_length=5)
    portas = models.CharField(choices=NIVEL, max_length=20)
    armarios = models.CharField("Armários", choices=NIVEL, max_length=20)
    vidros = models.CharField(choices=NIVEL, max_length=20)
    beliches = models.CharField(choices=NIVEL, max_length=20)
    mesa = models.CharField(choices=NIVEL, max_length=20)
    detalhes = models.TextField()
    motivo = models.CharField(choices=MOTIVOS, max_length=30)
    data = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('vistoria_lista',)

    class Meta:
        ordering = ['-data']
        verbose_name = "Vistoria"
        verbose_name_plural = "Vistorias"


class Limpeza(models.Model):
    AVAL = (
        (u'Ótimo', u'Ótimo'),
        (u'Bom', u'Bom'),
        (u'Ruim', u'Ruim'),
        (u'Muito ruim', u'Muito ruim')
    )
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
    )
    quarto = models.CharField(choices=ALOJA, max_length=10)
    semana_inicio = models.DateField()
    semana_fim = models.DateField()
    limpeza = models.CharField(max_length=20, choices=AVAL)
    lixo = models.CharField(max_length=20, choices=AVAL)
    verificado = models.DateTimeField()
    detalhes = models.TextField(max_length=1000,
                                null=True,
                                blank=True,
                                help_text='Anotações extras: sugestões, avisos, etc')
    servidor = models.ForeignKey(User)

    def __unicode__(self):
        return self.quarto

    class Meta:
        verbose_name = 'Limpeza'
        verbose_name_plural = 'Limpezas'

class Educacional(models.Model):
    aluno = models.OneToOneField(Aluno, primary_key=True)

    class Meta:
        ordering = ['aluno__nome']
        verbose_name = "Atendimento educacional"
        verbose_name_plural = "Atendimentos educacionais"

    def __unicode__(self):
        return str(self.aluno)

class Educacional_detalhe(models.Model):
    SETOR = (
        ('CGAE', 'CGAE'),
        ('CGE', 'CGE'),
        ('CAE', 'CAE'),
    )
    educacional = models.ForeignKey(Educacional, related_name='edu')
    ocorrencia = models.TextField("Ocorrência", max_length=10000, help_text="Descreva o atendimento")
    setor = models.CharField(max_length=5, choices=SETOR)
    servidor = models.ForeignKey(User)
    data = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "Atendimento %s"%str(self.id)

    class Meta:
        verbose_name = "Atendimento"
        verbose_name_plural = "Atendimentos"


class Prontuario(models.Model):
    aluno = models.OneToOneField(Aluno, primary_key=True)

    def __unicode__(self):
        return str(self.aluno)

    class Meta:
        ordering = ['aluno__nome']
        verbose_name = 'Prontuário'
        verbose_name_plural = 'Prontuários'

class Prontuario_detalhe(models.Model):
    prontuario = models.ForeignKey(Prontuario, related_name='pd')
    evento = models.TextField("Ocorrência", max_length=10000)
    servidor = models.ForeignKey(User)
    data = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "Atendimento %s"%str(self.id)

    class Meta:
        verbose_name = 'Atendimento ambulatorial'
        verbose_name_plural = 'Atendimentos ambulatoriais'

class Comunicados(models.Model):
    TIPO = (
        (u'Aviso', u'Aviso'),
        (u'Atendimento', u'Atendimento'),
        (u'Alerta', u'Alerta'),
        (u'Norma', u'Norma'),
        (u'Sugestão', u'Sugestão'),
        (u'Solicitação', u'Solicitação'),
        (u'Elogio', u'Elogio'),
        (u'Geral', u'Geral'),
    )
    tipo = models.CharField(max_length=50, choices=TIPO, default='Geral')
    aluno = models.ForeignKey(Aluno, blank=True, null=True)
    texto = models.TextField(max_length=10000)
    data = models.DateTimeField()
    servidor = models.ForeignKey(User)

    def get_absolute_url(self):
        return reverse('comunicado_lista')

    def __unicode__(self):
        return self.tipo

    class Meta:
        verbose_name = 'Comunicado'
        verbose_name_plural = 'Comunicados'

class Services(models.Model):
    ALOJA = (
	    (u'Geral', u'Geral'),
        (u'1_superior', u'1_superior'),
        (u'1_inferior', u'1_inferior'),
        (u'2_superior', u'2_superior'),
        (u'2_inferior', u'2_inferior'),
        (u'3_superior', u'3_superior'),
        (u'3_inferior', u'3_inferior'),
        (u'4_superior', u'4_superior'),
        (u'4_inferior', u'4_inferior'),
        (u'5_superior', u'5_superior'),
        (u'5_inferior', u'5_inferior'),
        (u'6_superior', u'6_superior'),
        (u'6_inferior', u'6_inferior'),
        (u'7_superior', u'7_superior'),
        (u'7_inferior', u'7_inferior'),
        (u'8_superior', u'8_superior'),
        (u'8_inferior', u'8_inferior'),
        (u'9_superior', u'9_superior'),
        (u'9_inferior', u'9_inferior'),
        (u'10_superior', u'10_superior'),
        (u'10_inferior', u'10_inferior'),
        (u'11_superior', u'11_superior'),
        (u'11_inferior', u'11_inferior'),
        (u'12_superior', u'12_superior'),
        (u'12_inferior', u'12_inferior'),
        (u'13_superior', u'13_superior'),
        (u'13_inferior', u'13_inferior'),
        (u'14_superior', u'14_superior'),
        (u'14_inferior', u'14_inferior'),
        (u'15_superior', u'15_superior'),
        (u'15_inferior', u'15_inferior'),
    )
    local = models.CharField(max_length=15, choices=ALOJA, editable=True, blank=True, null=True)
    atividade = models.TextField(max_length=10000)
    data_inicial = models.DateTimeField()
    servidor = models.ForeignKey(User)
    finalizado = models.BooleanField(default=False ,editable=True)
    data_final = models.DateTimeField(editable=True, null=True, blank=True)
    motivo = models.TextField(max_length=1000, editable=True, blank=True, null=True)

    def __str__(self):
        return self.local

    def __unicode__(self):
        return self.local

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

class Escala_Limpeza(models.Model):
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
    )
    semana_inicio = models.DateField("Data do início da semana")
    semana_fim = models.DateField("Data do final da semana")
    lixo = models.CharField(max_length=100, help_text="Alunos responsáveis para recolher os lixos durante a semana")
    limpeza = models.CharField(max_length=100, help_text="Alunos responsáveis pela limpeza geral durante a semana")
    quarto = models.CharField(choices=ALOJA, max_length=20)
    nota = models.IntegerField(blank=True, null=True, validators=[MaxValueValidator(5), MinValueValidator(1)])

    def __str__(self):
        return self.quarto


    class Meta:
        ordering = ['semana_inicio']
        verbose_name = 'Escala de limpeza'
        verbose_name_plural = 'Escalas de limpeza'

class Escala_Servidores(models.Model):
    SEMANA = (
        (u'Segunda-feira', u'Segunda-feira'),
        (u'Terça-feira', u'Terça-feira'),
        (u'Quarta-feira', u'Quarta-feira'),
        (u'Quinta-feira', u'Quinta-feira'),
        (u'Sexta-feira', u'Sexta-feira'),
    )
    dia_da_semana = models.CharField(choices=SEMANA, max_length=20)
    horario_de_inicio = models.TimeField("Horário de início")
    intervalo_inicio = models.TimeField("Horário inicial do intervalo", null=True, blank=True)
    intervalo_fim = models.TimeField("Horário final do intervalo", null=True, blank=True )
    horario_de_saida = models.TimeField("Horário de saída")
    servidor = models.ForeignKey(User)

    def __str__(self):
        return self.dia_da_semana

    def __unicode__(self):
        return self.dia_da_semana

    class Meta:
        verbose_name = 'Horário do servidor'
        verbose_name_plural = 'Horário dos servidores'
