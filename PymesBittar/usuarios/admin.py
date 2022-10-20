from django.contrib import admin
from usuarios.models import usuario

# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre_usuario','contraseña','rol',
    'vinculacion','tipo_usuario')
    search_fields = ('nombre_usuario','rol',
    'vinculacion','tipo_usuario')
    readonly_fields = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(usuario, UsuarioAdmin)
