from django.db import models

# Create your models here.

class Edificio(models.Model):
    TIPO_EDIFICIO = (
        ('Comercial', 'Comercial'),
        ('Residencial', 'Residencial')
    )
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    tipo = models.CharField(TIPO_EDIFICIO, max_length=20)
    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    numero_cuartos = models.IntegerField()
    nombre_propietario = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)  # Price in currency
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.numero} - {self.edificio.nombre}"