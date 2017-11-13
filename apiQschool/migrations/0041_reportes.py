# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-13 03:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiQschool', '0040_auto_20171112_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reportes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporte', models.TextField(blank=True, max_length=2047)),
                ('fecha', models.DateTimeField(auto_now_add=True, null=True)),
                ('modificado', models.DateTimeField(auto_now=True, null=True)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reportesAlumno', to='apiQschool.Perfil')),
                ('profesor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reportesGeneradosProfesor', to='apiQschool.Perfil')),
            ],
        ),
    ]
