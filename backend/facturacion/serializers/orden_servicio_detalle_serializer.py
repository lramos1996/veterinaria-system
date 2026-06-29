from rest_framework import serializers

from facturacion.models.ordenes_servicio import (
    OrdenServicio
)

from facturacion.models.detalle_ordenes_servicio import (
    DetalleOrdenServicio
)


class DetalleOrdenServicioMiniSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = DetalleOrdenServicio
        fields = [
            "id",
            "producto",
            "descripcion",
            "cantidad",
            "precio_unitario",
            "subtotal",
        ]


class OrdenServicioDetalleSerializer(
    serializers.ModelSerializer
):

    detalles = DetalleOrdenServicioMiniSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = OrdenServicio
        fields = [
            "id",
            "numero",
            "cliente",
            "mascota",
            "fecha",
            "observaciones",
            "total",
            "estado",
            "detalles",
        ]