from rest_framework import serializers

from facturacion.models.caja import (
    MovimientoCaja
)


class MovimientoCajaSerializer(
    serializers.ModelSerializer
):

    class Meta:
        model = MovimientoCaja
        fields = "__all__"