from django.urls import path
from .views import UsuarioView

urlpatterns = [
    path('usuarios/', UsuarioView.as_view(), name='usuarios_list'),
    path('usuarios/<correo>/<clave>', UsuarioView.as_view(), name='usuarios_process'),
    path('usuarios/<correo>', UsuarioView.as_view(), name='usuarios_process')
]