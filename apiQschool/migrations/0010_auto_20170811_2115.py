# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-11 21:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiQschool', '0009_auto_20170811_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='carne',
            field=models.CharField(blank=True, max_length=32, unique=True),
        ),
    ]
