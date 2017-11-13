from rest_framework import permissions
from django.contrib.auth.middleware import get_user
from django.utils.functional import SimpleLazyObject
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class AuthenticationMiddlewareJWT(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = SimpleLazyObject(lambda: self.__class__.get_jwt_user(request))
        return self.get_response(request)

    @staticmethod
    def get_jwt_user(request):
        user = get_user(request)
        if user.is_authenticated:
            return user
        jwt_authentication = JSONWebTokenAuthentication()
        if jwt_authentication.get_jwt_value(request):
            user, jwt = jwt_authentication.authenticate(request)
        return user
        
class IsOwnerOrReadOnlyCursos(permissions.BasePermission):
	# message = "Solo los catedraticos pueden crear/editar cursos"
	def has_object_permission(self,request,view,obj):
		if request.method in permissions.SAFE_METHODS:
				return True
		return obj.profesor.user == request.user

class IsOwnerOrReadOnlySubscripciones(permissions.BasePermission):
	# message = "Solo los catedraticos pueden crear/editar cursos"
	def has_object_permission(self,request,view,obj):
		if request.method in permissions.SAFE_METHODS:
				return True
		return obj.encargado.user == request.user

class IsOwnerOrReadOnlyActividades(permissions.BasePermission):
	message = "No puede crear/editar actividades de cursos ajenos"
	def has_object_permission(self,request,view,obj):
		if request.method in permissions.SAFE_METHODS:
				return True
		return obj.curso.profesor.user == request.user