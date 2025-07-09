from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import Edificio, Departamento

admin.register(Edificio)
admin.register(Departamento)
