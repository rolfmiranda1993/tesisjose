from django.db import models

# Create your models here.
class departamento(models.Model):
    nivel_jerarquia=(
        (u'1',u'Presidente'),
        (u'2',u'Gerente General'),
        (u'3',u'Gerente de Área'),
        (u'4',u'Responsable de Área'),
        (u'5',u'Supervisor'),
        (u'6',u'Colaborador'),
        )
    nombre = models.CharField(max_length=200, null=True, blank=True)
    jerarquia = models.CharField(max_length=2, choices=nivel_jerarquia)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class meta:
        Verbose_name = 'departamento'
        Verbose_name_plural = 'departamentos'
        #order_with_respect_to = 'nombre'
    
    def ___str__(self):
        return self.nombre