# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 19:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiQschool', '0025_entregaactividadalumno_calificad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entregaactividadalumno',
            old_name='calificad',
            new_name='calificado',
        ),
    ]