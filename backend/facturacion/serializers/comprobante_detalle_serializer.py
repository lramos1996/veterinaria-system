from rest_framework import serializers

from facturacion.models.comprobantes import (
    Comprobante
)

from facturacion.models.detalle_comprobantes import (
    DetalleComprobante
)


class DetalleComprobanteMiniSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = DetalleComprobante
        fields = [
            "id",
            "producto",
            "descripcion",
            "cantidad",
            "precio_unitario",
            "subtotal",
        ]


class ComprobanteDetalleSerializer(
    serializers.ModelSerializer
):

    detalles = DetalleComprobanteMiniSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Comprobante
        fields = [
            "id",
            "tipo",
            "orden_servicio",
            "serie",
            "numero",
            "fecha_emision",
            "subtotal",
            "igv",
            "total",
            "detalles",
        ]