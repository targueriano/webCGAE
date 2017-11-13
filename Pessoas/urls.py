from django.conf.urls import include, url
from . import views


aluno_patterns = [
    url(
        regex=r'^lista/$',
        view=views.lista_alunos,
        name='aluno_lista'
    ),
    url(
        regex=r'^atualizar/(?P<pk>\d+)/$',
        view=views.Aluno_update.as_view(),
        name='aluno_update'
    ),
    url(
        regex=r'^adicionar/$',
        view=views.Aluno_add.as_view(),
        name='aluno_add'
    ),
    url(
        regex=r'^adicionar/perfil/$',
        view=views.Aluno_add_perfil.as_view(),
        name='aluno_add_perfil'
    ),
    url(
        regex=r'^adicionar/familia/$',
        view=views.Aluno_add_familia.as_view(),
        name='aluno_add_familia'
    ),
    url(
        regex=r'^atualizar/perfil/(?P<pk>\d+)/$',
        view=views.Aluno_update_perfil.as_view(),
        name='aluno_update_perfil'
    ),
    url(
        regex=r'^atualizar/familia/(?P<pk>\d+)/$',
        view=views.Aluno_update_familia.as_view(),
        name='aluno_update_familia'
    ),
    url(
        regex=r'^adicionar/sucesso/$',
        view=views.aluno_add_sucesso,
        name="sucesso"
    )

]

fotovisor_patterns = [
    url(
        regex=r'^$',
        view=views.fotovisor,
        name='fotovisor'
    ),
    url(
        regex=r'^(?P<turma>\w+)/$',
        view=views.fotovisor_turma,
        name='fotovisor_turma'
    )
]

alojamento_patterns = [
    url(
        regex=r'^$',
        view=views.alojamento,
        name='alojamento'
    ),
    url(
        regex=r'^(?P<pk>(\d+|\w+)\w)/$',
        view=views.alojamento_quarto,
        name='alojamento_quarto'
    )
]

urlpatterns = [
    url(r'^$', views.home),
    url(r'^fotovisor/', include(fotovisor_patterns)),
    url(r'^aluno/', include(aluno_patterns)),
    url(r'^perfil/(?P<pk>\d+)/$', views.perfil_aluno, name='aluno_perfil'),
    url(r'^alojamento/', include(alojamento_patterns)),

]
