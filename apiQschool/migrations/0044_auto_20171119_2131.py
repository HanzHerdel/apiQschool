# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-19 21:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiQschool', '0043_asistenciascurso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistencia',
            name='alumno_curso',
        ),
        migrations.RemoveField(
            model_name='asistencia',
            name='fecha',
        ),
        migrations.RemoveField(
            model_name='asistencia',
            name='horario',
        ),
        migrations.AddField(
            model_name='asistencia',
            name='asistenciaCurso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='asistencia', to='apiQschool.AsistenciasCurso'),
            preserve_default=False,
        ),
    ]
