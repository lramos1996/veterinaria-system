from django.db import models

from veterinaria.models import Cliente
from veterinaria.models import Mascota


class OrdenServicio(models.Model):

    numero = models.CharField(
        max_length=20,
        unique=True
    )

    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT
    )

    mascota = models.ForeignKey(
        Mascota,
        on_delete=models.PROTECT
    )

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    observaciones = models.TextField(
        blank=True
    )

    total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    estado = models.CharField(
        max_length=20,
        default="PENDIENTE"
    )

    class Meta:
        verbose_name = "Orden de Servicio"
        verbose_name_plural = "Órdenes de Servicio"