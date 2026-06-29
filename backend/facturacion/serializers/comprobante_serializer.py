from rest_framework import serializers

from facturacion.models.comprobantes import (
    Comprobante
)


class ComprobanteSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = Comprobante
        fields = "__all__"