from rest_framework import serializers

from inventario.models.movimientos import (
    MovimientoInventario
)


class MovimientoInventarioSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = MovimientoInventario

        fields = "__all__"

    def validate_cantidad(
        self,
        value
    ):

        if value <= 0:

            raise serializers.ValidationError(
                "La cantidad debe ser mayor a cero"
            )

        return value