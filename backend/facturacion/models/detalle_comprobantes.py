from django.db import models

from .comprobantes import Comprobante


class DetalleComprobante(models.Model):

    comprobante = models.ForeignKey(
        Comprobante,
        on_delete=models.CASCADE
    )

    descripcion = models.CharField(
        max_length=250
    )

    cantidad = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    precio_unitario = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    class Meta:
        verbose_name = "Detalle Comprobante"
        verbose_name_plural = "Detalle Comprobantes"