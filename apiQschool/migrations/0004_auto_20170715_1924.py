# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiQschool', '0003_auto_20170715_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='grado',
            name='seccion',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G')], default='A', max_length=8),
        ),
        migrations.AlterField(
            model_name='grado',
            name='grado',
            field=models.CharField(choices=[('Primero', 'Primero'), ('Segundo', 'Segundo'), ('Tercero', 'Tercero'), ('Cuarto', 'Cuarto'), ('Quinto', 'Quinto'), ('Sexto', 'Sexto')], default='Primero', max_length=16),
        ),
        migrations.AlterField(
            model_name='grado',
            name='nivel',
            field=models.CharField(choices=[('primaria', 'primaria'), ('basico', 'basico'), ('diversificado', 'diversificado'), ('otro', 'otro')], default='basico', max_length=16),
        ),
    ]