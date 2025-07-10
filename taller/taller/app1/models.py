from django.db import models

# Create your models here.

class Edificio(models.Model):
    
    TIPO_EDIFICIO_CHOICES = (
        ( 'comercial', 'comercial'),
        ('residencial', 'residencial'),
    )

    nombre = models.CharField("Nombre", max_length=100)
    direccion = models.CharField("Dirección", max_length=200)
    ciudad = models.CharField("Ciudad", max_length=100)
    tipo = models.CharField(
        "Tipo de edificio",
        max_length=20,
        choices=TIPO_EDIFICIO_CHOICES
    )

    def __str__(self):
        return self.nombre


class Departamento(models.Model):
    nombre_propietario = models.CharField(
        "Nombre completo del propietario",
        max_length=100
    )
    costo = models.DecimalField(
        "Costo del departamento",
        max_digits=10,
        decimal_places=2
    )
    numero_cuartos = models.PositiveIntegerField("Número de cuartos")
    edificio = models.ForeignKey(
        Edificio,
        on_delete=models.CASCADE,
        related_name='departamentos'
    )

    def __str__(self):
        return f"Dpto. {self.numero_cuartos} - {self.edificio.nombre}"