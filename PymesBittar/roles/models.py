from random import choices
from django.db import models

# Create your models here.
class roles(models.Model):
    empleado_o_proveedor = models.CharField(max_length=250, null=True, blank=True)
    nombre_de_area = models.CharField(max_length=250, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class meta:
        Verbose_name = 'roles'
        Verbose_name_plural = 'roles'
        order_with_respect_to = 'empleado_o_proveedor'
    
    def ___str__(self):
        return self.empleado_o_proveedor