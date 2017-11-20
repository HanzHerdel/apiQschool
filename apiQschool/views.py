# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework import generics
from .permissions import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser, MultiPartParser, FileUploadParser,FormParser

# class InstitucionesList(generics.ListCreateAPIView):
#     queryset = Institucion.objects.all()
#     serializer_class = InstitucionSerializer


# class InstitucionDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Institucion.objects.all()
#     serializer_class = InstitucionSerializer

class HistorialDePagosList(generics.ListCreateAPIView):
    queryset = HistorialDePagos.objects.all()
    serializer_class = HistorialDePagosSerializer

class HistorialDePagosDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistorialDePagos.objects.all()
    serializer_class = HistorialDePagosSerializer

class ProfesorList(generics.ListCreateAPIView):
    queryset = Perfil.objects.filter(tipo='profesor')
    serializer_class = ProfesorSerializer

class ProfesorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perfil.objects.filter(tipo='profesor')
    serializer_class = ProfesorSerializer
    
class AlumnoList(generics.ListCreateAPIView):
    queryset = Perfil.objects.filter(tipo='alumno')
    serializer_class = AlumnoSerializer

class AlumnoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perfil.objects.filter(tipo='alumno')
    serializer_class = AlumnoSerializer

class PadreDeFamiliaList(generics.ListCreateAPIView):
    queryset = Perfil.objects.filter(tipo='padre')
    serializer_class = PadreDeFamiliaSerializer

class PadreDeFamiliaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perfil.objects.filter(tipo='padre')
    serializer_class = PadreDeFamiliaSerializer

class SubscripcionesList(generics.ListCreateAPIView):
    queryset = Subscripciones.objects.all()
    serializer_class = SubscripcionesSerializer
    def perform_create(self, serializer):
        serializer.save(encargado=self.request.user.perfilUsuario)


class SubscripcionesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subscripciones.objects.all()
    serializer_class = SubscripcionesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlySubscripciones)


class CursoList(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    def perform_create(self, serializer):
        serializer.save(profesor=self.request.user.perfilUsuario)

class CursoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyCursos)

class ActividadesCronograma(generics.ListCreateAPIView):
    queryset = ActividadesProgramadasCurso.objects.all()
    serializer_class = ActividadesProgramadasCursoSerializer

class ActividadesCronogramaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActividadesProgramadasCurso.objects.all()
    serializer_class = ActividadesProgramadasCursoSerializer

class CronogramaCursoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CronogramaCursoSerializer  

class CursosProfesorList(generics.ListCreateAPIView):
    serializer_class = CursoSerializer
    def get_queryset(self):
        #print self.request.user.perfilUsuario
        return Curso.objects.filter(profesor=self.request.user.perfilUsuario)

class AlumnosEnCurso(generics.ListAPIView):
    #queryset = AlumnoEnCurso.objects.all()
    serializer_class = AlumnoEnCursoSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return AlumnoEnCurso.objects.filter(curso=pk)

################# Crear Actividades en un curso
class CrearActividadesProfesor(generics.CreateAPIView):
    serializer_class = ActividadesProfesorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyActividades)

class ActividadesProfesorList(generics.ListAPIView):
    #queryset = ActividadCurso.objects.all()
    serializer_class = ActividadesProfesorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyActividades)
    def get_queryset(self):
        #print self.request.user.perfilUsuario
        return ActividadCurso.objects.filter(curso__profesor=self.request.user.perfilUsuario)

class Calificar(generics.CreateAPIView):
    serializer_class= CalificacionSerializer
    permission_classes= (IsAuthenticatedOrReadOnly,IsOwnerOrReadOnlyActividades)

############################################################################333
####################MATERIALES DE APOYO CRONOGRAMA CURSO estos son los parsers necesarios para la subida de archivos
class CrearMaterialesDeApoyo(generics.CreateAPIView):
    serializer_class = MaterialDeApoyoSerializer
    parser_classes =(MultiPartParser,FormParser)
    permission_classes =  (IsAuthenticatedOrReadOnly,)

class EditarCronogramaView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActividadesProgramadasCursoSerializer
    queryset= ActividadesProgramadasCurso.objects.all()

class EliminarMaterialesDeApoyo(generics.DestroyAPIView):
    serializer_class = MaterialDeApoyoSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
#########################################################################################
class EditarCalificacionView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CalificacionSerializer
    queryset= Calificacion.objects.all()

class PerfilList(generics.ListAPIView):
    #queryset = ActividadCurso.objects.all()
    serializer_class = PerfilSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnlyActividades)
    def get_queryset(self):
        return Perfil.objects.filter(user=self.request.user)

class HorarioProfesorList(generics.ListCreateAPIView):
    serializer_class = HorarioSerializer
    def get_queryset(self):
        #print self.request.user.perfilUsuario
        return Horario.objects.filter(curso__profesor=self.request.user.perfilUsuario)

class HorarioCursoList(generics.ListCreateAPIView):
    serializer_class = HorarioSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Horario.objects.filter(curso=pk)

class ActividadCursoList(generics.ListAPIView):
    serializer_class = ActividadesProfesorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,IsOwnerOrReadOnlyActividades)
    def get_queryset(self):
        pk = self.kwargs['pk']
        return ActividadCurso.objects.filter(curso=pk)
    # # def perform_create(self, serializer):
    #     print self
        #1serializer.save(curso=self.request.user.perfilUsuario)


class ActividadCursoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ActividadCurso.objects.all()
    serializer_class = ActividadCursoSerializer

class EntregaActividadEdit(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EntregaActividadAlumnoSerializer
    queryset= EntregaActividadAlumno.objects.all()



class EntregasActividad(generics.ListAPIView):
    serializer_class = EntregaActividadAlumnoSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return EntregaActividadAlumno.objects.filter(actividad=pk)

class HistorialAsistencia(generics.ListAPIView):
    serializer_class = HistorialAsistenciaSerializer
    def get_queryset(self):
        pk = self.kwargs['pk']
        return AlumnoEnCurso.objects.filter(curso=pk)

class CantidadAsistenciasCursoSerializer(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CantidadAsistenciasCursoSerializer
    queryset= Curso.objects.all()

class PunteoActividadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EntregaActividadAlumno.objects.all()
    serializer_class = SubirActividadesAlumnoSerializer

class AlumnoEnCursoList(generics.ListCreateAPIView):
    queryset = AlumnoEnCurso.objects.all()
    serializer_class = AlumnoEnCursoSerializer

class AlumnoEnCursoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AlumnoEnCurso.objects.all()
    serializer_class = AlumnoEnCursoSerializer

class GradoList(generics.ListCreateAPIView):
    queryset = Grado.objects.all()
    serializer_class = GradoSerializer

class GradoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grado.objects.all()
    serializer_class = GradoSerializer


#creacion de asistencias, se crea primero la AsistenciaCurso, luego se obtiene el id para crear las Asistencia de cada alumno
class AsistenciaList(APIView):
    def post (self, request,format=None):
        serializerAsistencia = AsistenciasCursoSerializer(data=request.data[u'asistencia'])#obtener la asistenciaCurso Del diccionario
        if serializerAsistencia.is_valid():
            serializerAsistencia.save()
            #print serializerAsistencia.data
            for item in request.data[u'asistencias']: #si se crea la asistenciaCurso obtendremos la id y la agregaremos a cada asistencia de alumno
                #print item
                item[u'asistenciaCurso']=serializerAsistencia.data[u'id']
            serializer = AsistenciaSerializer(data=request.data[u'asistencias'], many=True)
            if serializer.is_valid():
                   serializer.save()
                   return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializerAsistencia.errors, status=status.HTTP_400_BAD_REQUEST)

class AsistenciaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asistencia.objects.all()
    serializer_class = Asistencia
