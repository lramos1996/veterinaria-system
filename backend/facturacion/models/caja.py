from django.db import models

from .comprobantes import Comprobante
from .pagos import MetodoPago


class MovimientoCaja(models.Model):

    TIPOS = (
        ("INGRESO", "Ingreso"),
        ("EGRESO", "Egreso"),
    )

    comprobante = models.ForeignKey(
        Comprobante,
        on_delete=models.SET_NULL,
        null=True
    )

    metodo_pago = models.ForeignKey(
        MetodoPago,
        on_delete=models.PROTECT
    )

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS
    )

    monto = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    fecha = models.DateTimeField(
        auto_now_add=True
    )

    observacion = models.TextField(
        blank=True
    )

    class Meta:
        verbose_name = "Movimiento Caja"
        verbose_name_plural = "Movimientos Caja"