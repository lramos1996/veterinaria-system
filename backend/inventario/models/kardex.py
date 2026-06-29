from django.db import models

from .productos import Producto


class Kardex(models.Model):

    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT
    )

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    tipo_movimiento = models.CharField(
        max_length=20
    )

    cantidad = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    stock_anterior = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    stock_nuevo = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    referencia = models.CharField(
        max_length=200,
        blank=True
    )

    class Meta:
        verbose_name = "Kardex"
        verbose_name_plural = "Kardex"