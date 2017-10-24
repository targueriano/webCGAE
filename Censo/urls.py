from django.conf.urls import include, url
from . import views


censo_patterns = [
    url(
        regex=r'^alunos/$',
        view=views.censo_alunos,
        name='censo_alunos'
    ),
    url(
        regex=r'^rendimento/$',
        view=views.censo_rendimento,
        name='censo_rendimento'
    ),
    url(
        regex=r'^cidades/$',
        view=views.censo_cidades,
        name='censo_cidades'
    ),

]

urlpatterns = [
    url(r'^censo/', include(censo_patterns)),

]
