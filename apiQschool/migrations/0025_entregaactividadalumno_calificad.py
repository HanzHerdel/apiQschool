# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiQschool', '0024_actividadcurso_calificado'),
    ]

    operations = [
        migrations.AddField(
            model_name='entregaactividadalumno',
            name='calificad',
            field=models.BooleanField(default=False),
        ),
    ]