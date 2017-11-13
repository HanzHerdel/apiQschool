# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 21:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiQschool', '0010_auto_20170811_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='carne',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='alumnoencurso',
            unique_together=set([('alumno', 'curso')]),
        ),
    ]
