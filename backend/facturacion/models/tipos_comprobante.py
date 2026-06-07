from django.db import models


class TipoComprobante(models.Model):

    nombre = models.CharField(
        max_length=50,
        unique=True
    )

    abreviatura = models.CharField(
        max_length=10
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Tipo Comprobante"
        verbose_name_plural = "Tipos Comprobante"