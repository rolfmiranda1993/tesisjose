from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class miembroModel(models.Model):
    miembro_fields = models.CharField(max_length=200)

class miembro(models.Model):
    EST = ((u'1',u'Soltero'),
    (u'2',u'Casado'),
    (u'3',u'Viudo'),
    (u'4',u'Divorciado'),
    )
    HIJ = ((u'1',u'Si'),
    (u'2',u'No'),
    )
    GEN = ((u'1',u'Efectivo'),
    (u'H',u'Hombre'),
    (u'M',u'Mujer'),
    (u'PNM',u'Prefiero no mencionarlo'),
    )

    nombres = models.CharField(max_length=250, null=True, blank=True)
    apellidos = models.CharField(max_length=250, null=True, blank=True)
    nacionalidad = models.CharField(max_length=250, null=True, blank=True)
    numero_de_documento = models.CharField(max_length=250, null=True, blank=True)
    fecha_de_nacimiento = models.CharField(max_length=50, null=True, blank=True)
    telefono_particular = models.CharField(max_length=250, null=True, blank=True)
    telefono_corporativo = models.CharField(max_length=250, null=True, blank=True)
    mail_particular = models.CharField(max_length=250, null=True, blank=True)
    mail_corporativo = models.CharField(max_length=250, null=True, blank=True)
    fecha_de_ingreso = models.CharField(max_length=50, null=True, blank=True)
    fecha_de_salida = models.CharField(max_length=50, null=True, blank=True)
    motivo_de_salida = models.CharField(max_length=250, null=True, blank=True)
    cargo = models.CharField(max_length=250, null=True, blank=True)
    notas_adicionales = models.CharField(max_length=250, null=True, blank=True)
    contribuyente_set = models.CharField(max_length=20, choices=HIJ)
    estado_civil= models.CharField(max_length=250, choices=EST)
    hijos = models.CharField(max_length=250, choices=HIJ)
    genero = models.CharField(max_length=250, choices=GEN)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class meta:
        Verbose_name = 'miembro'
        Verbose_name_plural = 'miembros'
        order_with_respect_to = 'nombres'
    
    def nombre_completo(self):
        return "{} {}".format(self.nombres,self.apellidos)

    def ___str__(self):
        return self.nombre_completo()