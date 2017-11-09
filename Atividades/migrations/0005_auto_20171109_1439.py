# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Atividades', '0004_auto_20171106_2237'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vistoria',
            options={'ordering': ['-data'], 'verbose_name': 'Vistoria', 'verbose_name_plural': 'Vistorias'},
        ),
        migrations.RemoveField(
            model_name='vistoria',
            name='vistoria',
        ),
        migrations.AddField(
            model_name='vistoria',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vistoria',
            name='data',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='vistoria',
            name='motivo',
            field=models.CharField(choices=[('Pedido de troca', 'Pedido de troca'), ('Interesse da administra\xe7\xe3o', 'Interesse da administra\xe7\xe3o')], max_length=30),
        ),
    ]
