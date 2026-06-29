from rest_framework import serializers

from facturacion.models.detalle_ordenes_servicio import (
    DetalleOrdenServicio
)


class DetalleOrdenServicioSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = DetalleOrdenServicio
        fields = "__all__"