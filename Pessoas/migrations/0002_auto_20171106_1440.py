# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-06 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pessoas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='alojamento',
            field=models.CharField(blank=True, choices=[('1A', '1A'), ('1B', '1B'), ('1C', '1C'), ('1D', '1D'), ('1E', '1E'), ('1F', '1F'), ('2A', '2A'), ('2B', '2B'), ('2C', '2C'), ('2D', '2D'), ('2E', '2E'), ('2F', '2F'), ('3A', '3A'), ('3B', '3B'), ('3C', '3C'), ('3D', '3D'), ('3E', '3E'), ('3F', '3F'), ('4A', '4A'), ('4B', '4B'), ('4C', '4C'), ('4D', '4D'), ('4E', '4E'), ('4F', '4F'), ('5A', '5A'), ('5B', '5B'), ('5C', '5C'), ('5D', '5D'), ('5E', '5E'), ('5F', '5F'), ('6A', '6A'), ('6B', '6B'), ('6C', '6C'), ('6D', '6D'), ('6E', '6E'), ('6F', '6F'), ('7A', '7A'), ('7B', '7B'), ('7C', '7C'), ('7D', '7D'), ('7E', '7E'), ('7F', '7F'), ('8A', '8A'), ('8B', '8B'), ('8C', '8C'), ('8D', '8D'), ('8E', '8E'), ('8F', '8F'), ('9A', '9A'), ('9B', '9B'), ('9C', '9C'), ('9D', '9D'), ('9E', '9E'), ('9F', '9F'), ('10A', '10A'), ('10B', '10B'), ('10C', '10C'), ('10D', '10D'), ('10E', '10E'), ('10F', '10F'), ('11A', '11A'), ('11B', '11B'), ('11C', '11C'), ('11D', '11D'), ('11E', '11E'), ('11F', '11F'), ('12A', '12A'), ('12B', '12B'), ('12C', '12C'), ('12D', '12D'), ('12E', '12E'), ('12F', '12F'), ('13A', '13A'), ('13B', '13B'), ('13C', '13C'), ('13D', '13D'), ('13E', '13E'), ('13F', '13F'), ('14A', '14A'), ('14B', '14B'), ('14C', '14C'), ('14D', '14D'), ('14E', '14E'), ('14F', '14F'), ('15A', '15A'), ('15B', '15B'), ('15C', '15C'), ('15D', '15D'), ('15E', '15E'), ('15F', '15F'), ('ZooI', 'ZooI'), ('ZooII', 'ZooII'), ('ZooIII', 'ZooIII')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='perfil_do_aluno',
            name='objetivos',
            field=models.CharField(blank=True, choices=[('Curso superior na \xe1rea agr\xedcola', 'Curso superior na \xe1rea agr\xedcola'), ('Curso superior fora da \xe1rea agr\xedcola', 'Curso superior fora da \xe1rea agr\xedcola'), ('Continuar trabalho familiar na agricultura', 'Continuar trabalho familiar na agricultura'), ('Trabalhar na \xe1rea do curso', 'Trabalhar na \xe1rea do curso'), ('Outro', 'Outro'), ('N\xe3o sabe responder', 'N\xe3o sabe responder')], help_text='Objetivo ao completar o curso', max_length=300, null=True),
        ),
    ]