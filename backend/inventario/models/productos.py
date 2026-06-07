from django.db import models

from .categorias import CategoriaProducto


class Producto(models.Model):

    codigo = models.CharField(
        max_length=30,
        unique=True
    )

    nombre = models.CharField(
        max_length=200
    )

    categoria = models.ForeignKey(
        CategoriaProducto,
        on_delete=models.PROTECT
    )

    stock_actual = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    stock_minimo = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    costo = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    precio_venta = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    activo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"