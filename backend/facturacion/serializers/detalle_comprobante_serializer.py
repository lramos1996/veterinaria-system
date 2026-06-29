from rest_framework import serializers

from facturacion.models.detalle_comprobantes import (
    DetalleComprobante
)


class DetalleComprobanteSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = DetalleComprobante
        fields = "__all__"