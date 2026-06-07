from django.db import models


class Proveedor(models.Model):

    razon_social = models.CharField(
        max_length=200
    )

    ruc = models.CharField(
        max_length=20,
        unique=True
    )

    telefono = models.CharField(
        max_length=20,
        blank=True
    )

    correo = models.EmailField(
        blank=True
    )

    direccion = models.TextField(
        blank=True
    )

    activo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.razon_social

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"