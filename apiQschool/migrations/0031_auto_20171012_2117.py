# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-12 21:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiQschool', '0030_auto_20171011_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calificacion',
            name='actividad',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='calificacion', to='apiQschool.EntregaActividadAlumno'),
        ),
    ]
