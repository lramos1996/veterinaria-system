from django.db import models


class Cliente(models.Model):

    nombres = models.CharField(max_length=100)

    apellidos = models.CharField(max_length=100)

    documento = models.CharField(
        max_length=20,
        unique=True
    )

    telefono = models.CharField(max_length=20)

    correo = models.EmailField(
        blank=True
    )

    direccion = models.TextField(
        blank=True
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"