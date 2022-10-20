from django.contrib import admin
from departamento.models import departamento

# Register your models here.
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'jerarquia')
    search_fields = ('nombre', 'jerarquia')
    readonly_fields = ('created', 'updated')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(departamento, DepartamentoAdmin)