from django.conf.urls import include, url
from . import views

comunicado_patterns = [
    url(regex=r'^lista/$',
        view=views.comunicados,
        name='comunicado_lista'
	),
 	url(regex=r'^novo/$',
        view=views.comunicado_novo,
        name='comunicado_novo'
	),
    url(regex=r'^detalhe/(?P<pk>\d+)/$',
        view=views.comunicado_detalhe,
        name='comunicado_detalhe'
	),
 	url(regex=r'^(?P<pk>\d+)/$',
        view=views.Comunicado_update.as_view(),
        name='comunicado_update'
	),

]



relatorio_patterns = [
    url(regex=r'^lista/$',
        view=views.lista_relatorios,
        name='relatorio_lista'
    ),
    url(regex=r'^novo/$',
        view=views.relatorio_novo,
        name='relatorio_novo'
    ),
    url(
        regex=r'^detalhe/(?P<pk>\d+)/$',
        view=views.relatorio_detalhe,
        name='relatorio_detalhe'
    ),
    url(regex=r'^(?P<pk>\d+)/$',
        view=views.Relatorio_update.as_view(),
        name='relatorio_update'
    ),

]


atendimento_patterns = [
    url(
        regex=r'^ambulatorial/prontuarios/$',
        view=views.prontuario_lista,
        name='prontuario_lista'
    ),
    url(
        regex=r'^ambulatorial/novo/$',
        view=views.Prontuario_add.as_view(),
        name='prontuario_add'
    ),
    url(
        regex=r'^ambulatorial/prontuario/(?P<pk>\d+)/$',
        view=views.prontuario_detalhe,
        name='prontuario_detalhe'
    ),
    url(
        regex=r'^ambulatorial/prontuario/editar/(?P<pk>\d+)/$',
        view=views.Prontuario_detalhe_update.as_view(),
        name='prontuario_update'
    ),
    url(
        regex=r'^educacional/lista/$',
        view=views.educacional_lista,
        name='educacional_lista'
    ),
    url(
        regex=r'^educacional/editar/(?P<pk>\d+)/$',
        view=views.Educacional_detalhe_update.as_view(),
        name='educacional_update'
    ),
    url(
        regex=r'^educacional/novo/$',
        view=views.Educacional_add.as_view(),
        name='educacional_add'
    ),
    url(
        regex=r'^educacional/(?P<pk>\d+)/$',
        view=views.educacional_detalhe,
        name='educacional_detalhe'
    )

]

escala_patterns = [
    url(
        regex=r'^limpeza/$',
        view=views.escala_limpeza,
        name='escala_limpeza'
    ),
    url(
        regex=r'^limpeza/(?P<pk>\d+\w,\d+\w,\d+\w)/$',
        view=views.escala_limpeza_quarto,
        name='escala_limpeza_quarto'
    ),
    url(
        regex=r'^cgae/$',
        view=views.escala_cgae,
        name='escala_cgae'
    ),
    url(
        regex=r'^cgae/(?P<pk>\d)/$',
        view=views.escala_cgae_select,
        name='escala_cgae_select'
    )
]

urlpatterns = [
    url(r'^comunicado/', include(comunicado_patterns)),
    url(r'^atendimento/', include(atendimento_patterns)),
    url(r'^escala/', include(escala_patterns)),
    url(r'^relatorio/', include(relatorio_patterns)),
    url(r'^vistorias/$', views.lista_vistorias),
    url(r'^accounts/login/$', views.acesso_msg, name='acesso_negado'),
    url(r'^gerar/denuncia/(?P<pk>\d+)$', views.gerar_pdf_denuncia, name='gerar_denuncia'),
    url(r'^gerar/comunicacao/(?P<pk>\d+)$', views.gerar_pdf_comunicacao, name='gerar_comunicacao'),
    url(r'^gerar/comunicado/(?P<pk>\d+)$', views.gerar_pdf_comunicado, name='gerar_comunicado'),
]
