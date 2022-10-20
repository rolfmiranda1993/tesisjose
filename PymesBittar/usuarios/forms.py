from django import forms
from usuarios.models import usuario

class AddUsuarioForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ('nombre_usuario','contraseña','rol','vinculacion','tipo_usuario')
        labels = {
            'nombre_usuario' : 'Nombre de usuario',
            'contraseña' : 'Contraseña: ',
            'rol' : 'Rol del usuario: ',
            'vinculacion' : 'Vinculación: ',
            'tipo_usuario' : 'Tipo de usuario: '
        }

class EditUsuarioForm(forms.ModelForm):
    class Meta:
        model = usuario
        fields = ('nombre_usuario','contraseña','rol','vinculacion','tipo_usuario')
        labels = {
            'nombre_usuario': 'Nombre de usuario',
            'contraseña' : 'Contraseña: ',
            'rol' : 'Rol del usuario: ',
            'vinculacion' : 'Vinculación: ',
            'tipo_usuario' : 'Tipo de usuario: '
        }

        widgets = {
            'nombre_usuario' : forms.TextInput(attrs={'type' : 'text', 'id' : 'nombre_usuario_editar'}),
            'contraseña' : forms.TextInput(attrs={'id' : 'contraseña_editar'}),
            'rol' : forms.TextInput(attrs={'id' : 'rol_editar'}),
            'vinculacion' : forms.TextInput(attrs={'id' : 'vinculacion_editar'}),
            'tipo_usuario' : forms.TextInput(attrs={'id' : 'tipo_usuario_editar'})
        }