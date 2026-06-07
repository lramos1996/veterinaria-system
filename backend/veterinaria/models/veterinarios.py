from django.db import models


class Veterinario(models.Model):

    nombres = models.CharField(
        max_length=100
    )

    apellidos = models.CharField(
        max_length=100
    )

    colegiatura = models.CharField(
        max_length=50,
        unique=True
    )

    telefono = models.CharField(
        max_length=20,
        blank=True
    )

    correo = models.EmailField(
        blank=True
    )

    especialidad = models.CharField(
        max_length=100,
        blank=True
    )

    activo = models.BooleanField(
        default=True
    )

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

    class Meta:
        verbose_name = "Veterinario"
        verbose_name_plural = "Veterinarios"