from django.contrib import admin
from rubros.models import rubro

# Register your models here.
class RubroAdmin(admin.ModelAdmin):
    list_display = ('area', 'nombre')
    search_fields = ('area', 'nombre')
    readonly_fields = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(rubro, RubroAdmin)