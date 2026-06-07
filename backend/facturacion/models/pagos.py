from django.db import models


class MetodoPago(models.Model):

    nombre = models.CharField(
        max_length=100
    )

    activo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Método de Pago"
        verbose_name_plural = "Métodos de Pago"