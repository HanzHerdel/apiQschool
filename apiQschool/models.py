# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

#########################librerias para la automatizacion de perfil
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
# modelo de instutuciones

#modificacion de usuario django
# CARGO_CHOICES=(('director','director'),
# 		('subdirector','subdirector'),
# 		('secretario','secretario'),
# 		('otro','otro'))
DIA_CHOICES=(('lunes','lunes'),('martes','martes'),
			('miercoles','miercoles'),('jueves','jueves'),('viernes','viernes'),
			('sabado','sabado'),('domingo','domingo'))
USER_CHOICES=(('alumno','alumno'),
		('profesor','profesor'),
		('administracion','administracion'),
		('padre','padre'))
NIVEL_CHOICES=(('primaria','primaria'),
		('basico','basico'),
		('diversificado','diversificado'),
		('otro','otro'))
TIPO_CHOICES=(('tarea','tarea'),
		('trabajo','trabajo'),
		('investigacion','investigacion'),
		('examen parcial','examen parcial'),
		('examen','examen'),
		('proyecto','proyecto'),
		('otro','otro'))
GRADOS_CHOICES=(
	('Primero','Primero'),('Segundo','Segundo'),('Tercero','Tercero'),('Cuarto','Cuarto'),('Quinto','Quinto'),('Sexto','Sexto'))
SECCION_CHOICES=(('A','A'),('B','B'),('C','C'),('D','D'),('E','E'),('F','F'),('G','G'))

class Institucion(models.Model):
	nombre = models.CharField(max_length=64)
	logo1 = models.ImageField(upload_to='logos',blank=True,null=True)
	logo2 = models.ImageField(upload_to='logos',blank=True,null=True)
	logo3 = models.ImageField(upload_to='logos',blank=True,null=True)
	logo4 = models.ImageField(upload_to='logos',blank=True,null=True)
	descripcion= models.TextField(blank=True,max_length=2047)
	direccion = models.TextField(blank=True,max_length=224)
	tel1=models.CharField(blank=True,max_length=16)
	tel2=models.CharField(blank=True,max_length=16,)
	telefonoDirector=models.CharField(blank=True,max_length=16)
	fechaDePagos = models.DateTimeField(blank=True,null=True)
	mora= models.BooleanField(default=False)
	pagoMensual= models.DecimalField(blank=True,max_digits=7 ,decimal_places=2,null=True)
	def __str__(self):
		return self.nombre

#facturas de Quetzaltech
class HistorialDePagos(models.Model):
	noFactura=models.CharField(max_length=64)
	institucion =models.ForeignKey(Institucion,on_delete=models.CASCADE, related_name='facturas')
	fecha = models.DateTimeField(auto_now_add=True)
	cantidad =models.DecimalField(max_digits=7 ,decimal_places=2)
	concepto =models.CharField(blank=True,max_length=64)
	def __str__(self):
		return self.noFactura

#alumnos de una institucion
class Grado(models.Model):
	nivel = models.CharField(choices=NIVEL_CHOICES,default='basico',max_length=16)
	especifico = models.CharField(blank=True,max_length=32,default='.')
	grado = models.CharField(choices=GRADOS_CHOICES,default='Primero',max_length=16)
	institucion=models.ForeignKey(Institucion,on_delete=models.CASCADE, related_name='gradosInstitucion')
	seccion=models.CharField(choices=SECCION_CHOICES,default='A',max_length=8)
	def __str__(self):
		identi = ' %s %s %s ' % (self.grado, self.nivel, self.especifico)
		return identi.strip()

#profesores de una institucion !!!!Anulados por unificacion de usuarios
class Perfil(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfilUsuario')
	tipo = models.CharField(choices=USER_CHOICES, default='alumno',max_length=16)
	institucion=models.ForeignKey(Institucion,on_delete=models.CASCADE, related_name='perfiles',null=True)
	tel=models.CharField(blank=True,max_length=16)
	cel=models.CharField(blank=True,max_length=16)
	direccion= models.TextField(blank=True,max_length=512)
	carne=models.CharField(max_length=32,unique=True)
	telEmergencia=models.CharField(blank=True,max_length=16)
	grado =models.ForeignKey(Grado ,on_delete=models.SET_NULL, related_name='alumnosDeGrado',null=True,blank=True)
	def __str__(self):
		identi = '%s %s %s %s' % (self.tipo, self.user.first_name, self.user.last_name, self.carne)
		return identi.strip()

@receiver(post_save, sender=User)
def create_or_update_user_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    instance.perfilUsuario.save()


# class Alumno(models.Model):
# 	user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='perfilAlumno')
# 	grado =models.ForeignKey(Grado ,on_delete=models.CASCADE, related_name='alumnosDeGrado',null=True)
# 	institucion=models.ForeignKey(Institucion,on_delete=models.CASCADE, related_name='alumnos')
# 	tel=models.CharField(blank=True,max_length=16)
# 	cel=models.CharField(blank=True,max_length=16)
# 	direccion= models.TextField(blank=True,max_length=224)
# 	telEmergencia=models.CharField(blank=True,max_length=16)
# 	carne=models.CharField(blank=True,max_length=32)
# 	def __str__(self):
# 		return self.user.get_full_name()

# #padres o encargados de estudiantes
# class PadreDeFamilia(models.Model):
# 	user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='perfilPadre')
# 	tel=models.CharField(blank=True,max_length=16)
# 	cel=models.CharField(blank=True,max_length=16)
# 	direccion= models.TextField(blank=True,max_length=224)
# 	anotaciones=models.CharField(blank=True,max_length=512)
# 	def __str__(self):
# 		identi = '%s %s' % ('Encargado:', self.user.get_full_name())
# 		return self.anotaciones.strip()
class Reportes(models.Model):
	profesor=models.ForeignKey(Perfil,on_delete=models.SET_NULL, related_name='reportesGeneradosProfesor',null=True)
	alumno = models.ForeignKey(Perfil,on_delete=models.CASCADE, related_name='reportesAlumno' )
	reporte= models.TextField(blank=True,max_length=2047)
	fecha=models.DateTimeField(auto_now_add=True,null=True, blank=True)
	modificado=models.DateTimeField(auto_now=True,null=True, blank=True)

class Subscripciones(models.Model):
	encargado=models.ForeignKey(Perfil,on_delete=models.CASCADE, related_name='subscripcionespadre')
	alumno=models.ForeignKey(Perfil,on_delete=models.CASCADE, related_name='subscripcionesAlumno' )
	class Meta:
		unique_together = ['encargado','alumno']
	def __str__(self):
		identi = '%s %s' % (self.encargado, self.alumno)
		return identi.strip()

# class Clase(models.Model):
# 	nombre=models.CharField(blank=True,max_length=32)
# 	grado=models.ForeignKey(Grado,on_delete=models.SET_NULL, related_name='claseGrado',null=True)
# 	def __str__(self):
# 		return self.nombre
    
#curso de un profesor
class Curso(models.Model):
	titulo = models.CharField(blank=True,max_length=64)
	grado =models.ForeignKey(Grado,on_delete=models.SET_NULL, related_name='cursosDeGrado',null=True)
	profesor=models.ForeignKey(Perfil,on_delete=models.SET_NULL, related_name='cursosProfesor',null=True)
	descripcion= models.TextField(blank=True,max_length=2047)
	institucion=models.ForeignKey(Institucion,on_delete=models.CASCADE, related_name='cursosInstitucion')
	clase = models.CharField(blank=True,max_length=32)
	def __str__(self):
		return self.titulo

class Horario(models.Model):
	curso = models.ForeignKey(Curso,on_delete=models.CASCADE, related_name='horarioCursos')
	grado = models.ForeignKey(Grado,on_delete=models.CASCADE, related_name='horarioGrado')
	dia = models.CharField(choices=DIA_CHOICES,default='lunes',max_length=16)
	hora = models.TimeField(auto_now=False, auto_now_add=False,editable=True,blank=True)
#	fecha = models.DateTimeField(blank=True,null=True)
	def __str__(self):
		identi = ' %s %s %s ' % (self.curso, self.dia, self.hora)
		return identi.strip()

#actividades para el cronograma del curso
def generar_carpeta(instance, filename):
	return "{institucion}/Material_de_apollo/{curso}{grado}/{file}".format(institucion=instance.actividadProgramada.curso.institucion, 
		curso=instance.actividadProgramada.curso.titulo,grado=instance.actividadProgramada.curso.grado, file=filename)

class ActividadesProgramadasCurso(models.Model):
	curso=models.ForeignKey(Curso,on_delete=models.CASCADE, related_name='programa')
	fechaDeInicio = models.DateTimeField(blank=True,null=True)
	fechaDeFinalizacion = models.DateTimeField(blank=True,null=True)
	titulo=models.CharField(blank=True,max_length=64)
	descripcion=models.TextField(blank=True,max_length=224)
	objetivos=models.TextField(blank=True,max_length=224)
	valoracion = models.DecimalField(default=0,max_digits=5, decimal_places=2)
	modificado=models.DateTimeField(auto_now=True,null=True, blank=True)
	def __str__(self):
		return self.titulo

class MaterialDeApoyo(models.Model):
	archivo=models.FileField(upload_to=generar_carpeta,null=True,blank=True)
	actividadProgramada = models.ForeignKey(ActividadesProgramadasCurso, on_delete=models.CASCADE,related_name='materialesDeApoyo')


#actividades (examenes trabajos parciales) de un curso
class ActividadCurso(models.Model):
	curso=models.ForeignKey(Curso,on_delete=models.CASCADE, related_name='ActividadesDeCurso')
	titulo=models.CharField(blank=True,max_length=64)
	tipo=models.CharField(choices=TIPO_CHOICES,max_length=64,default="tarea")
	fechaDeEntrega =models.DateTimeField(blank=True,null=True)
	fechaDeAplazo = models.DateTimeField(blank=True,null=True)
	punteo = models.DecimalField(default=0,max_digits=5, decimal_places=2)
	punteoExtra = models.DecimalField(default=0,max_digits=5, decimal_places=2)
	descripcion = models.TextField(blank=True,max_length=224)
	anotaciones = models.TextField(blank=True,max_length=224,default="Ninguna")
	archivos = models.BooleanField(default=False)
	calificado = models.BooleanField(default=False)
	def __str__(self):
		identi = '%s %s' % (self.titulo, self.curso.titulo)
		return identi.strip()

#creacion de los objetos EntregaActividadAlumno (entregas de actividades de alumno) automaticamente al momento de crear una actividad de curso
@receiver(post_save, sender=ActividadCurso)
def create_actividad(sender, instance, created, **kwargs):
    if created:
    	alumnos = AlumnoEnCurso.objects.filter(curso=instance.curso)
    	for alumno in alumnos:
    		ob=EntregaActividadAlumno.objects.create(actividad=instance,alumno=alumno.alumno)
    		ob.save()
    		#print ob 

def generar_carpeta_entrega(instance, filename):
	return "{institucion}/engregaDeaActividades/{curso}{grado}/{actividad}/{file}".format(institucion=instance.alumno.institucion.nombre,
		curso=instance.actividad.curso.titulo,grado=instance.actividad.curso.grado,actividad=instance.actividad.titulo, file=filename)


#punteo que recive el alumno por alguna actividad en especifico
class EntregaActividadAlumno(models.Model):
	actividad=models.ForeignKey(ActividadCurso,on_delete=models.CASCADE, related_name='entrega')
	alumno = models.ForeignKey(Perfil,on_delete=models.CASCADE, related_name='punteosAlumno')
	comentario=models.TextField(blank=True,max_length=224,default="Ninguno")
	imagen = models.ImageField(upload_to=generar_carpeta_entrega,null=True, blank=True)
	archivo = models.FileField(upload_to=generar_carpeta_entrega,null=True,blank=True)
	entregado = models.BooleanField(default=False)
	calificado = models.BooleanField(default=False)
	fecha=models.DateTimeField(auto_now_add=True,null=True, blank=True)
	modificado=models.DateTimeField(auto_now=True,null=True, blank=True)
	class Meta:
		unique_together = ['actividad','alumno']
	def __str__(self):
		identi = '%s %s' % (self.actividad, self.alumno)
		return identi.strip()

class Calificacion(models.Model):
	punteo= models.DecimalField(blank=True,max_digits=7 ,decimal_places=2,null=True)
	punteoExtra= models.DecimalField(blank=True,max_digits=7 ,decimal_places=2,null=True)
	comentario=models.TextField(blank=True,max_length=224,default="Ninguno")
	entregaActividadAlumno=models.OneToOneField(EntregaActividadAlumno,on_delete=models.CASCADE, related_name='calificacion')
	fecha=models.DateTimeField(auto_now_add=True,null=True, blank=True)
	modificado=models.DateTimeField(auto_now=True,null=True, blank=True)
	# def __str__(self):
	# 	identi = '%s %s %s' % (self.actividad.titulo, self.actividad.curso, self.alumno.user.username)
	# 	return identi.strip()
 
 #cambio de estado de la entrega de actividad a true  
@receiver(post_save, sender=Calificacion)
def patch_entregaactividad(sender, instance, created, **kwargs):
    if created:
    	entregaActividad = EntregaActividadAlumno.objects.get(id=instance.entregaActividadAlumno.pk)
    	print (entregaActividad)
    	entregaActividad.calificado=True;
    	entregaActividad.save()
    	print (entregaActividad)


#alumno en curso
class AlumnoEnCurso(models.Model):
	alumno=models.ForeignKey(Perfil,on_delete=models.CASCADE, related_name='alumnosEnCurso')
	curso=models.ForeignKey(Curso,on_delete=models.CASCADE, related_name='CursosDeAlumno')
	def __str__(self):
		curso_alumno = '%s %s' % (self.alumno, self.curso)
		return curso_alumno.strip()
	class Meta:
		unique_together = ['alumno','curso']

class AsistenciasCurso(models.Model):#asistencia base para llevar un mejor control sobre las asistencias creadas, es unica para cada fecha
	curso = models.ForeignKey(Curso,on_delete=models.CASCADE, related_name='asistenciasCurso')
	fecha = models.DateTimeField(blank=True,null=True)
	horario =models.ForeignKey(Horario,on_delete=models.CASCADE, related_name='asistenciasHorario',null=True)
	def __str__(self):
		valor = '%s %s' % (self.curso, self.fecha)
		return valor.strip()

class Asistencia(models.Model):#asistencia alumno relacionado con asistenciaCurso
	alumno=models.ForeignKey(Perfil,on_delete=models.CASCADE, related_name='asistenciaAlumno')
	asistencia=models.BooleanField(default=True)
#	horario=models.ForeignKey(Horario,on_delete=models.CASCADE, related_name='asistenciaHorario',null=True)
	modificado=models.DateTimeField(auto_now=True,null=True, blank=True)
	asistenciaCurso=models.ForeignKey(AsistenciasCurso,on_delete=models.CASCADE, related_name='asistencia')
	def __str__(self):
		return self.alumno.user.first_name
	class Meta:
		unique_together = ['alumno','asistenciaCurso']
	# def __str__(self):
	# 	identi = '%s %s' % (self.alumno_curso.alumno.user.username, self.alumno_curso.curso.titulo)
	# 	return identi.strip()


	


"""
#staff de la institucion 
class Administracion(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='perfilAdministrador')
	institucion=models.ForeignKey(Institucion,on_delete=models.CASCADE, related_name='personal')
	tel=models.CharField(blank=True,max_length=16)
	cel=models.CharField(blank=True,max_length=16)
	direccion= models.TextField(blank=True,max_length=512)
	cargo=models.CharField(choices=CARGO_CHOICES,default='director',max_length=16)
	def __str__(self):
		identi = '%s %s' % (self.institucion.nombre, self.cargo)
		return identi.strip()"""








