from rest_framework import serializers

from inventario.models.proveedores import (
    Proveedor
)


class ProveedorSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Proveedor

        fields = "__all__"

    def validate_ruc(
        self,
        value
    ):

        if len(value) != 11:

            raise serializers.ValidationError(
                "El RUC debe tener 11 dígitos"
            )

        return value