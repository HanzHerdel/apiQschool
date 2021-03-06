# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 17:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apiQschool', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('alumno', 'alumno'), ('profesor', 'profesor'), ('administracion', 'administracion'), ('padre', 'padre')], default='alumno', max_length=16)),
                ('tel', models.CharField(blank=True, max_length=16)),
                ('cel', models.CharField(blank=True, max_length=16)),
                ('direccion', models.TextField(blank=True, max_length=512)),
                ('carne', models.CharField(blank=True, max_length=32)),
                ('telEmergencia', models.CharField(blank=True, max_length=16)),
                ('grado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='alumnosDeGrado', to='apiQschool.Grado')),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='perfiles', to='apiQschool.Institucion')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfilUsuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='grado',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='institucion',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='user',
        ),
        migrations.RemoveField(
            model_name='padredefamilia',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='institucion',
        ),
        migrations.RemoveField(
            model_name='profesor',
            name='user',
        ),
        migrations.AlterField(
            model_name='alumnoencurso',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alumnosEnCurso', to='apiQschool.Perfil'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='grado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cursosDeGrado', to='apiQschool.Grado'),
        ),
        migrations.AlterField(
            model_name='curso',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursosProfesor', to='apiQschool.Perfil'),
        ),
        migrations.AlterField(
            model_name='punteoalumno',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='punteosAlumno', to='apiQschool.Perfil'),
        ),
        migrations.AlterField(
            model_name='subscripciones',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscripcionesAlumno', to='apiQschool.Perfil'),
        ),
        migrations.AlterField(
            model_name='subscripciones',
            name='encargado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscripcionespadre', to='apiQschool.Perfil'),
        ),
        migrations.DeleteModel(
            name='Alumno',
        ),
        migrations.DeleteModel(
            name='PadreDeFamilia',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]
