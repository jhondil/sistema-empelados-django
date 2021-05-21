from django import forms
from django.forms.widgets import Widget
from .models import Empleado


class EmpleadoForms(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'full_name',
            'job',
            'departamento',
            'image',
            'habilidades',
        )
        widgets ={
            'habilidades':forms.CheckboxSelectMultiple()
        }
