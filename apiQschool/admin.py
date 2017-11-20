# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

admin.site.register(Institucion)
admin.site.register(HistorialDePagos)
admin.site.register(Perfil)
admin.site.register(Subscripciones)
admin.site.register(Curso)
admin.site.register(ActividadesProgramadasCurso)
admin.site.register(ActividadCurso)
admin.site.register(EntregaActividadAlumno)
admin.site.register(AlumnoEnCurso)
admin.site.register(Grado)
admin.site.register(Asistencia)
admin.site.register(Horario)
admin.site.register(Calificacion)
admin.site.register(MaterialDeApoyo)
admin.site.register(Reportes)
admin.site.register(AsistenciasCurso)
# Register your models here.
class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'Perfil'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (PerfilInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)
UserAdmin.list_display = ('username','email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff','perfilUsuario')


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)