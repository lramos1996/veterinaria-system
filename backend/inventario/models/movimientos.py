from django.db import models

from .productos import Producto


class MovimientoInventario(models.Model):

    TIPOS = (
        ("ENTRADA", "Entrada"),
        ("SALIDA", "Salida"),
        ("AJUSTE", "Ajuste"),
    )

    producto = models.ForeignKey(
        Producto,
        on_delete=models.CASCADE
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS
    )

    cantidad = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    observacion = models.TextField(
        blank=True
    )

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Movimiento Inventario"
        verbose_name_plural = "Movimientos Inventario"