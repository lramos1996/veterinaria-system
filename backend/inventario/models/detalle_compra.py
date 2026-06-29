from django.db import models

from .compras import (
    Compra
)

from .productos import (
    Producto
)


class DetalleCompra(models.Model):

    compra = models.ForeignKey(
        Compra,
        on_delete=models.CASCADE,
        related_name="detalles"
    )

    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT
    )

    cantidad = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    costo_unitario = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    subtotal = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    class Meta:

        verbose_name = (
            "Detalle Compra"
        )

        verbose_name_plural = (
            "Detalles Compra"
        )