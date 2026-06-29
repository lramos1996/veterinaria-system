from django.db import models

from .mascotas import Mascota
from .veterinarios import Veterinario


class HistoriaClinica(models.Model):

    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE,
        related_name="historias_clinicas"
    )

    veterinario = models.ForeignKey(
        Veterinario,
        on_delete=models.SET_NULL,
        null=True,
        related_name="historias_clinicas"
    )

    peso = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )

    temperatura = models.DecimalField(
        max_digits=4,
        decimal_places=1,
        null=True,
        blank=True
    )

    anamnesis = models.TextField()

    diagnostico = models.TextField()

    tratamiento = models.TextField()

    observaciones = models.TextField(
        blank=True
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )
    
    fecha_atencion = models.DateTimeField()

    def __str__(self):

        return (
            f"{self.mascota.nombre} - "
            f"{self.fecha_atencion}"
        )
    class Meta:
        verbose_name = "Historia Clínica"
        verbose_name_plural = "Historias Clínicas"
        ordering = [
            "-fecha_atencion"
        ]
