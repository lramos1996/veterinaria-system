from django.db import models

from .mascotas import Mascota
from .veterinarios import Veterinario


class Cita(models.Model):

    ESTADOS = (
        ("PROGRAMADA", "Programada"),
        ("ATENDIDA", "Atendida"),
        ("CANCELADA", "Cancelada"),
    )

    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.CASCADE
    )

    veterinario = models.ForeignKey(
        Veterinario,
        on_delete=models.CASCADE
    )

    fecha = models.DateField()

    hora = models.TimeField()

    motivo = models.TextField()

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default="PROGRAMADA"
    )

    observaciones = models.TextField(
        blank=True
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.mascota} - {self.fecha}"

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"