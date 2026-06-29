from django.db import models

from .comprobantes import Comprobante

from inventario.models.productos import (
    Producto
)


class DetalleComprobante(models.Model):

    comprobante = models.ForeignKey(
        Comprobante,
        on_delete=models.CASCADE,
        related_name="detalles"
    )

    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        null=True,
        blank=True
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
        verbose_name_plural = (
            "Detalle Comprobantes"
        )