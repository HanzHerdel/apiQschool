# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-14 23:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiQschool', '0012_actividadcurso_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividadcurso',
            name='archivo',
            field=models.FileField(default='actividades/archivos/none.txt', upload_to='actividades/archivos/'),
        ),
    ]