from rest_framework import serializers

from facturacion.models.tipos_comprobante import (
    TipoComprobante
)


class TipoComprobanteSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = TipoComprobante

        fields = "__all__"