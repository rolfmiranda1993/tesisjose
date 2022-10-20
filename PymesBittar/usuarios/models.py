from django.db import models

# Create your models here.
class usuario(models.Model):
    TIPO = ((u'1',u'Master'),
    (u'2',u'Editor'),
    (u'3',u'Financiero'),
    (u'4',u'Visualizador'),
    )
    ROL = ((u'1',u'Colaborador'),
    (u'2',u'Proveedor'),
    )
        
    nombre_usuario = models.CharField(max_length=250, null=False, blank=False)
    contraseña = models.CharField(max_length=250, null=False, blank=False)
    rol = models.CharField(max_length=50, choices=ROL)
    vinculacion = models.CharField(max_length=250, null=True, blank=True)
    tipo_usuario = models.CharField(max_length=50, choices=TIPO)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class meta:
        Verbose_name = 'usuario'
        Verbose_name_plural = 'usuarios'
        order_with_respect_to = 'nombre_usuario'
    
    def ___str__(self):
        return self.nombre_usuario