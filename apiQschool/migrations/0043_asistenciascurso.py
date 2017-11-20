# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-19 21:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiQschool', '0042_auto_20171113_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsistenciasCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asistenciasCurso', to='apiQschool.Curso')),
                ('horario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='asistenciasHorario', to='apiQschool.Horario')),
            ],
        ),
    ]