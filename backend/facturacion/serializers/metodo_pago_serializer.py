from rest_framework import serializers

from facturacion.models.pagos import (
    MetodoPago
)


class MetodoPagoSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = MetodoPago

        fields = "__all__"