from django.urls import path
from . import views

urlpatterns = [
    path('',views.usuarios_views, name = 'Usuarios'),
    path('add_usuario/',views.add_usuarios_views, name = 'AddUsuario'),
    path('edit_usuario/',views.edit_usuarios_views, name = 'EditUsuario'),
    path('delete_usuario/',views.delete_usuarios_views, name = 'DeleteUsuario'),
]