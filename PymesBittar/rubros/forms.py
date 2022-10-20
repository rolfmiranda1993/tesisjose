from django import forms
from rubros.models import rubro

class AddRubroForm(forms.ModelForm):
    class Meta:
        model = rubro
        fields = ('area','nombre')
        labels = {
            'area' : 'Area: ',
            'nombre' : 'Nombre: ',
        }

class EditRubroForm(forms.ModelForm):
    class Meta:
        model = rubro
        fields = ('area','nombre')
        labels = {
            'area' : 'Area: ',
            'nombre' : 'Nombre: ',
        }

        widgets = {
            'area' : forms.TextInput(attrs={'type' : 'text', 'id' : 'area_editar'}),
            'nombre' : forms.TextInput(attrs={'id' : 'nombre_editar'}),
        }