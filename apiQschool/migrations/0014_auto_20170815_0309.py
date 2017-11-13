# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-15 03:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apiQschool', '0013_actividadcurso_archivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntregaActividadAlumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('comentarioAlumno', models.TextField(blank=True, max_length=224)),
                ('comentarioProfesor', models.TextField(blank=True, max_length=224)),
                ('punteoExtra', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
                ('imagen', models.ImageField(default='actividades/imagenes/none.jpg', upload_to='actividades/imagenes/')),
                ('archivo', models.FileField(default='actividades/archivos/none.txt', upload_to='actividades/archivos/')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='punteoalumno',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='punteoalumno',
            name='actividad',
        ),
        migrations.RemoveField(
            model_name='punteoalumno',
            name='alumno',
        ),
        migrations.RemoveField(
            model_name='actividadcurso',
            name='archivo',
        ),
        migrations.RemoveField(
            model_name='actividadcurso',
            name='imagen',
        ),
        migrations.DeleteModel(
            name='PunteoAlumno',
        ),
        migrations.AddField(
            model_name='entregaactividadalumno',
            name='actividad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actividades', to='apiQschool.ActividadCurso'),
        ),
        migrations.AddField(
            model_name='entregaactividadalumno',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='punteosAlumno', to='apiQschool.Perfil'),
        ),
        migrations.AlterUniqueTogether(
            name='entregaactividadalumno',
            unique_together=set([('actividad', 'alumno')]),
        ),
    ]
