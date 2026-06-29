from django.db import models

from facturacion.models.ordenes_servicio import (
    OrdenServicio
)

from inventario.models.productos import (
    Producto
)


class DetalleOrdenServicio(models.Model):

    orden_servicio = models.ForeignKey(
        OrdenServicio,
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
        verbose_name = "Detalle Orden de Servicio"
        verbose_name_plural = (
            "Detalles de Órdenes de Servicio"
        )

    def __str__(self):
        return (
            f"{self.orden_servicio.numero} - "
            f"{self.descripcion}"
        )