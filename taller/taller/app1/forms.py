from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms
from app1.models import Edificio
from app1.models import Departamento

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese nombre del edificio'),
            'direccion': _('Ingrese dirección'),
            'ciudad': _('Ingrese ciudad'),
            'tipo': _('Seleccione tipo de edificio'),
        }

    def clean_nombre(self):
        valor = self.cleaned_data.get('nombre', '').strip()
        if len(valor) < 3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres.")
        return valor

    def clean_direccion(self):
        valor = self.cleaned_data.get('direccion', '').strip()
        if len(valor) < 5:
            raise forms.ValidationError("La dirección debe tener al menos 5 caracteres.")
        return valor

    def clean_ciudad(self):
        valor = self.cleaned_data.get('ciudad', '').strip()
        if not valor.isalpha():
            raise forms.ValidationError("La ciudad debe contener solo letras.")
        return valor

class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_propietario', 'costo', 'numero_cuartos', 'edificio']
        labels = {
            'nombre_propietario': 'Nombre completo del propietario',
            'costo': 'Costo del departamento',
            'numero_cuartos': 'Número de cuartos',
            'edificio': 'Edificio',
        }