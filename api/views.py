from io import StringIO
from django.http.response import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario
import json

# Create your views here.

class UsuarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, correo='', clave=''):
        if(correo!=''):
            users=list(Usuario.objects.filter(correo=correo).values())
            if len(users)>0:
                user=users[0]
                stringUser = json.dumps(user)
                jsonUser= json.loads(stringUser)
                claveUsuario = jsonUser['clave']
                if(clave==claveUsuario):
                    datos = {'message': "Conexion exitosa"}
                    return JsonResponse(datos)
                else:
                    datos = {'message': 'usuario o contraseña incorrecta'}
                    return JsonResponse(datos)
            else:
                datos = {'message': "No se encontro el usuario"}       
                return JsonResponse(datos)
        else:
            usuarios = list(Usuario.objects.values())
            if len(usuarios) > 0:
                datos = {'message': "exitoso", 'usuarios': usuarios}
            else:
                datos = {'message': "usuario no encontrado"}
            return JsonResponse(datos)

    def post(self, request):
        jsonEntrada = json.loads(request.body)
        Usuario.objects.create(nombre=jsonEntrada['nombre'],apellido=jsonEntrada['apellido'],correo=jsonEntrada['correo'],clave=jsonEntrada['clave'])
        datos = {'message':"exitoso"}
        return JsonResponse(datos)

    def put(self, request, correo):
        jd = json.loads(request.body)
        usuarios=list(Usuario.objects.filter(correo=correo).values())
        if len(usuarios) >0:
            usuario = Usuario.objects.get(correo=correo)
            usuario.nombre =jd['nombre']
            usuario.apellido =jd['apellido']
            usuario.clave =jd['clave']
            usuario.save()
            datos = {'message' : 'Usuario Modificado'}
        else:
            datos = {'message': "No se encontro el usuario"}
        return JsonResponse(datos)    

    def delete(self, request, correo):
        usuarios=list(Usuario.objects.filter(correo=correo).values())
        if len(usuarios) >0:
            Usuario.objects.filter(correo=correo).delete()
            datos = {'message' : 'Usuario Eliminado'}
        else:
            datos = {'message': "No se encontro el usuario"}
        return JsonResponse(datos)    
        


