from django.db import models

# Create your models here.
class egresos(models.Model):
    rubro = models.CharField(max_length=200, null=True, blank=True)
    forma_de_pago = models.CharField(max_length=200, unique=True, null=True, blank=True)
    tipo_de_pago = models.CharField(max_length=200, unique=True, null=True, blank=True)
    nombre_de_pago = models.CharField(max_length=200, unique=True, null=True, blank=True)
    titular_de_pago = models.CharField(max_length=200, unique=True, null=True, blank=True)
    monto_de_pago = models.CharField(max_length=200, unique=True, null=True, blank=True)
    responsable = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class meta:
        Verbose_name = 'egresos'
        Verbose_name_plural = 'egresos'
        order_with_respect_to = 'rubro'
    
    def ___str__(self):
        return self.rubro