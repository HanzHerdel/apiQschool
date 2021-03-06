# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-23 17:13
from __future__ import unicode_literals

import apiQschool.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiQschool', '0035_auto_20171019_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividadesprogramadascurso',
            name='materialDeApoyo',
            field=models.FileField(blank=True, null=True, upload_to=apiQschool.models.generar_carpeta),
        ),
        migrations.AlterField(
            model_name='entregaactividadalumno',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to=apiQschool.models.generar_carpeta_entrega),
        ),
        migrations.AlterField(
            model_name='entregaactividadalumno',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=apiQschool.models.generar_carpeta_entrega),
        ),
    ]
