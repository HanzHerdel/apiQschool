# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 21:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiQschool', '0005_auto_20170721_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('lunes', 'lunes'), ('martes', 'martes'), ('miercoles', 'miercoles'), ('jueves', 'jueves'), ('viernes', 'viernes'), ('sabado', 'sabado'), ('domingo', 'domingo')], default='lunes', max_length=16)),
                ('hora', models.TimeField(blank=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horarioCursos', to='apiQschool.Curso')),
                ('grado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='horarioGrado', to='apiQschool.Grado')),
            ],
        ),
    ]