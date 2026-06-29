from rest_framework import serializers

from facturacion.models.ordenes_servicio import (
    OrdenServicio
)


class OrdenServicioSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = OrdenServicio
        fields = "__all__"