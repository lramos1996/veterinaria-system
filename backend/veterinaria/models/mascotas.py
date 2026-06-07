from django.db import models
from .clientes import Cliente


class Mascota(models.Model):

    SEXO_CHOICES = (
        ("M", "Macho"),
        ("H", "Hembra"),
    )

    propietario = models.ForeignKey(
        Cliente,
        on_delete=models.CASCADE,
        related_name="mascotas"
    )

    nombre = models.CharField(max_length=100)

    especie = models.CharField(max_length=50)

    raza = models.CharField(max_length=100)

    sexo = models.CharField(
        max_length=1,
        choices=SEXO_CHOICES
    )

    fecha_nacimiento = models.DateField(
        null=True,
        blank=True
    )

    peso = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )

    color = models.CharField(
        max_length=50,
        blank=True
    )

    observaciones = models.TextField(
        blank=True
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"