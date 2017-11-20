"""qschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from apiQschool import views
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from django.views.static import serve
#from schoolApi import views
#from rest_framework import routers
#router = routers.DefaultRouter()

urlpatterns = [
    # url(r'^instituciones/$',views.InstitucionesList.as_view()),
    # url(r'^instituciones/(?P<pk>[0-9]+)/$',views.InstitucionDetail.as_view()),
    url(r'^pagos/$',views.HistorialDePagosList.as_view()),
    url(r'^pagos/(?P<pk>[0-9]+)/$',views.HistorialDePagosDetail.as_view()),
    url(r'^profesores/$',views.ProfesorList.as_view()),
    url(r'^profesores/(?P<pk>[0-9]+)/$',views.ProfesorDetail.as_view()),
    url(r'^alumnos/$',views.AlumnoList.as_view()),
    url(r'^alumnos/(?P<pk>[0-9]+)/$',views.AlumnoDetail.as_view()),
    url(r'^subscripciones/$',views.SubscripcionesList.as_view()),
    url(r'^subscripciones/(?P<pk>[0-9]+)/$',views.SubscripcionesDetail.as_view()),
    url(r'^padresdefamilia/$',views.PadreDeFamiliaList.as_view()),
    url(r'^padresdefamilia/(?P<pk>[0-9]+)/$',views.PadreDeFamiliaDetail.as_view()),
    url(r'^perfil/$',views.PerfilList.as_view()),
    url(r'^alumnosencurso/(?P<pk>[0-9]+)/$',views.AlumnosEnCurso.as_view()),

    url(r'^cursos/$',views.CursoList.as_view()),
    url(r'^cursos/(?P<pk>[0-9]+)/$',views.CursoDetail.as_view()),
    url(r'^cursosprofesor/$',views.CursosProfesorList.as_view()),   

    url(r'^cronogramacursos/$',views.ActividadesCronograma.as_view()),#crearNuevos Programas
    url(r'^editarcronograma/(?P<pk>[0-9]+)/$',views.EditarCronogramaView.as_view()),#Edicion y Eliminacion de programa
    url(r'^cronogramacursos/(?P<pk>[0-9]+)/$',views.CronogramaCursoDetail.as_view()),#obtencion de Cronograma en un curos
    url(r'^materialcronograma/$',views.CrearMaterialesDeApoyo.as_view()),#crear material de apoyo para actividad de cronograma
   

    url(r'^eliminarmaterialcronograma/$',views.EliminarMaterialesDeApoyo.as_view()),#eliminar material de apoyo para actividad de cronograma

    url(r'^crearactividadcurso/$',views.CrearActividadesProfesor.as_view()),    
    url(r'^actividades/(?P<pk>[0-9]+)/$',views.ActividadCursoDetail.as_view()),
    
    url(r'^listaactividadcurso/(?P<pk>[0-9]+)/$',views.ActividadCursoList.as_view()),
    url(r'^historialasistencia/(?P<pk>[0-9]+)/$',views.HistorialAsistencia.as_view()),
    url(r'^asistenciascurso/(?P<pk>[0-9]+)/$',views.CantidadAsistenciasCursoSerializer.as_view()),


    url(r'^editarentrega/(?P<pk>[0-9]+)/$',views.EntregaActividadEdit.as_view()),
    url(r'^entregasactividad/(?P<pk>[0-9]+)/$',views.EntregasActividad.as_view()),
    url(r'^calificar/$',views.Calificar.as_view()),
    url(r'^editarcalificacion/(?P<pk>[0-9]+)/$',views.EditarCalificacionView.as_view()),
    
    url(r'^punteos/(?P<pk>[0-9]+)/$',views.PunteoActividadDetail.as_view()),
    url(r'^alumnoencursos/$',views.AlumnoEnCursoList.as_view()),
    url(r'^alumnoencurso/(?P<pk>[0-9]+)/$',views.AlumnoEnCursoDetail.as_view()),
    url(r'^grados/$',views.GradoList.as_view()),
    url(r'^grados/(?P<pk>[0-9]+)/$',views.GradoDetail.as_view()),
    url(r'^crearasistencia/$',views.AsistenciaList.as_view()),
    url(r'^asistencia/(?P<pk>[0-9]+)/$',views.AsistenciaDetail.as_view()),
    url(r'^cronograma/(?P<pk>[0-9]+)/$',views.CronogramaCursoDetail.as_view()),
    url(r'^horarioprofesor/$',views.HorarioProfesorList.as_view()),
    url(r'^horariocurso/(?P<pk>[0-9]+)/$',views.HorarioCursoList.as_view()),
    url(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT,}),

    url(r'^admin/', admin.site.urls),
    url(r'^tokenauth/', obtain_jwt_token),
    url(r'^tokenverify/', verify_jwt_token),
    url(r'^tokenrefresh/', refresh_jwt_token),
       # url(r'^', include(router.urls)),
    # url(r'^autenticacion/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
if  settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)