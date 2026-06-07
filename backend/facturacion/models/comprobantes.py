from django.db import models

from .tipos_comprobante import TipoComprobante
from .ordenes_servicio import OrdenServicio


class Comprobante(models.Model):

    tipo = models.ForeignKey(
        TipoComprobante,
        on_delete=models.PROTECT
    )

    orden_servicio = models.ForeignKey(
        OrdenServicio,
        on_delete=models.PROTECT
    )

    serie = models.CharField(
        max_length=10
    )

    numero = models.CharField(
        max_length=20
    )

    fecha_emision = models.DateTimeField(
        auto_now_add=True
    )

    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    igv = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    total = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    class Meta:
        verbose_name = "Comprobante"
        verbose_name_plural = "Comprobantes"