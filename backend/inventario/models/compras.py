from django.db import models

from .proveedores import (
    Proveedor
)


class Compra(models.Model):

    proveedor = models.ForeignKey(
        Proveedor,
        on_delete=models.PROTECT
    )

    numero_documento = models.CharField(
        max_length=50
    )

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    total = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    observacion = models.TextField(
        blank=True
    )

    def __str__(self):

        return self.numero_documento

    class Meta:

        verbose_name = "Compra"

        verbose_name_plural = "Compras" 