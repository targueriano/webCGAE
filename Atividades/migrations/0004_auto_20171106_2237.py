# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 00:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Atividades', '0003_auto_20171106_2235'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prontuario',
            options={'ordering': ['aluno__nome'], 'verbose_name': 'Prontu\xe1rio', 'verbose_name_plural': 'Prontu\xe1rios'},
        ),
    ]
