from rest_framework import serializers
from rest_framework import permissions
from django.contrib.auth.models import User
from models import (Institucion,HistorialDePagos,
	Perfil,Grado,Subscripciones,
	Curso,ActividadesProgramadasCurso,ActividadCurso,
	EntregaActividadAlumno,AlumnoEnCurso,Asistencia,Horario,Calificacion,MaterialDeApoyo,
	USER_CHOICES)

#innesesario proximo a ser eliminado 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class PerfilSerializer(serializers.ModelSerializer):
	user=UserSerializer(many=False, read_only=True)
	class Meta:
		model= Perfil
		fields = ['tipo','id','carne','grado','user']


# #innesesario proximo a ser eliminado 
# class UserRelatedSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username')

#innesesario proximo a ser eliminado 
class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = ('__all__')
class HistorialDePagosSerializer(serializers.ModelSerializer):
	#institucion = serializers.SlugRelatedField(slug_field='nombre',queryset=Institucion.objects.all())
	class Meta:
		model = HistorialDePagos
		fields = '__all__'
		#extra_fields = ['institucion']
class ProfesorSerializer(serializers.ModelSerializer):
	user=serializers.SlugRelatedField(slug_field='username',queryset=User.objects.filter(perfilUsuario__tipo='profesor'))
	#institucion = serializers.SlugRelatedField(slug_field='nombre',queryset=Institucion.objects.all())
	class Meta:
		model = Perfil
		fields = ('__all__')
		extra_fields = ['user']
class AlumnoSerializer(serializers.ModelSerializer):
	user=serializers.SlugRelatedField(slug_field='username',queryset=User.objects.filter(perfilUsuario__tipo='alumno'))
	#institucion = serializers.SlugRelatedField(slug_field='nombre',queryset=Institucion.objects.all())
	class Meta:
		model = Perfil
		fields = ('__all__')
		extra_fields = ['user']
class PadreDeFamiliaSerializer(serializers.ModelSerializer):
	user=serializers.SlugRelatedField(slug_field='username',queryset=User.objects.filter(perfilUsuario__tipo='padre'))
	class Meta:
		model = Perfil
		fields = ('__all__')
		extra_fields= ['user']
class SubscripcionesSerializer(serializers.ModelSerializer):
	encargado=serializers.ReadOnlyField(source='encargado.user.username')
	alumno=serializers.SlugRelatedField(slug_field='id',queryset=Perfil.objects.filter(tipo='alumno'))
	class Meta:
		model = Subscripciones
		fields = ('encargado','alumno')

class CursoSerializer(serializers.ModelSerializer):
	#profesor = ProfesorCursoSerializer()
	profesor=serializers.ReadOnlyField(source='profesor.user.username')
	class Meta:
		model = Curso
		fields = ('__all__')
        extra_fields = ['profesor']
	# def create(self, validated_data):
	# 	profesor_data = validated_data.pop('profesor')
	# 	curso = Curso.objects.create(profesor=profesor_data, **validated_data)
	# 	return curso
	
#innesesario proximo a ser eliminado 

class MaterialDeApoyoSerializer(serializers.ModelSerializer):
	class Meta:
		model = MaterialDeApoyo
		fields = ('__all__')

#necesario recivir un curso para poder desplegar sus actividades chau bye noches adios
class ActividadesProgramadasCursoSerializer(serializers.ModelSerializer):
	materialesDeApoyo = MaterialDeApoyoSerializer(many=True,read_only=True)
	class Meta:
		model = ActividadesProgramadasCurso
		fields = ('__all__')
		extra_fields = ['materialesDeApoyo']

class GradoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Grado
		fields = ('__all__')



class CronogramaCursoSerializer(serializers.ModelSerializer):
	programa = ActividadesProgramadasCursoSerializer(many=True,read_only=True)
	grado = GradoSerializer(many=False, read_only=True)
#	grado = GradoSerializer(read_only=True)
	titulo = serializers.CharField(read_only=True)
	#programa = serializers.PrimaryKeyRelatedField(many=True,queryset=ActividadesProgramadasCurso.objects.all())
	class Meta:
		model = Curso
		fields = ['programa','titulo','grado']

### serializer de actividades muestra
# class ActividadCursoSerializer(serializers.ModelSerializer):
# 	curso = serializers.SlugRelatedField(slug_field='id',queryset=Curso.objects.all())
# 	class Meta:
# 		model = ActividadCurso
# 		fields = ('__all__')

################## serializer para la creacion de actividad de cursos dentro de curso
class ActividadesProfesorSerializer(serializers.ModelSerializer):
	punteo = serializers.DecimalField(default=0,max_digits=5, decimal_places=2,required=False,allow_null=True)
	punteoExtra = serializers.DecimalField(default=0,max_digits=5, decimal_places=2,required=False,allow_null=True)
	class Meta:
		model = ActividadCurso
		fields = ('__all__')

class SubirActividadesAlumnoSerializer(serializers.ModelSerializer):
	imagen=serializers.ImageField(max_length=64, allow_empty_file=True)
	archivo=serializers.FileField(max_length=64, allow_empty_file=True)
	class Meta:
		model = ActividadCurso
		fields = ('__all__')
		extra_fields = ['imagen','archivo']

####################### obtencion de cursos del profesor
class CursosProfesorSerializer(serializers.Serializer):
	def get(self, *args, **kwargs):
		print self.context['request'].user
		cursos=Curso.objects.filter(profesor__user=self.context['request'].user)

	# def __init__(self, *args, **kwargs):
	# 	    super(CursosProfesorSerializer, self).__init__(*args, **kwargs)
	# 	    request_user = self.context['request'].user
	# 	    self.queryset = Curso.objects.filter(profesor__user=request_user)
	# 	    print self.queryset

	# 	    # self.fields['cursos'].queryset = Curso.objects.filter(profesor__user=request_user)

#no funciona mal pero puede eliminarse, se hizo al momento de aprender a serializar
#su funcion es devolver unicamente los cursos que pertenecen al profesor
class ActividadCursoSerializer(serializers.ModelSerializer):
	class Meta:
		model = ActividadCurso
		fields=('__all__')

class CrearActividadCursoSerializer(serializers.Serializer):
	curso=serializers.SlugRelatedField(slug_field='titulo',queryset=Curso.objects.all())
	titulo=serializers.CharField()
	fechaDeEntrega = serializers.DateTimeField()
	fechaDeAplazo = serializers.DateTimeField(required=False)
	punteo = serializers.IntegerField(required=False)
	puteoExtra = serializers.IntegerField(required=False)
	descripcion=serializers.CharField(required=False)
	anotaciones=serializers.CharField(required=False)
	def __init__(self, *args, **kwargs):
	    super(CrearActividadCursoSerializer, self).__init__(*args, **kwargs)
	    #request_user = self.context['request'].user
	    print self.context['request'].user
	    self.fields['curso'].queryset = Curso.objects.filter(profesor__user=self.context['request'].user)
	def create(self, validated_data):
		return ActividadCurso.objects.create(**validated_data)

class HorarioSerializer(serializers.ModelSerializer):
	 class Meta:
	 	model = Horario
	 	fields=('__all__')


class CalificacionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Calificacion
		fields= ('__all__')

class EntregaActividadAlumnoSerializer(serializers.ModelSerializer):
	calificacion=CalificacionSerializer(many=False, read_only=True)
	class Meta:
		model = EntregaActividadAlumno
		fields = ('__all__')
		extra_fields = ['calificacion']

class AlumnoEnCursoSerializer(serializers.ModelSerializer):
	alumno = PerfilSerializer(many=False, read_only=True)
	class Meta:
		model = AlumnoEnCurso
		fields = ['curso','alumno','id']

class AlumnoEnCurso4AsistenciaSerializer(serializers.ModelSerializer):
	class Meta:
		model = AlumnoEnCurso
		fields = ('__all__')

class AsistenciaListSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        asistencia = [Asistencia(**item) for item in validated_data]
        return Asistencia.objects.bulk_create(asistencia)

class AsistenciaSerializer(serializers.ModelSerializer):
    
    class Meta:
    	fields=('__all__')
    	model = Asistencia
        list_serializer_class = AsistenciaListSerializer

# class AsistenciaSerializer(serializers.ModelSerializer):
# 	#alumno_curso=AlumnoEnCurso4AsistenciaSerializer(many=True,read_only=True)
# 	#nombreAlumno=serializers.SlugRelatedField(slug_field='')
# 	class Meta:
# 		model = Asistencia
# 		fields = ('__all__')

		

