# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-08 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiQschool', '0006_horario'),
    ]

    operations = [
        migrations.AddField(
            model_name='horario',
            name='fecha',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
