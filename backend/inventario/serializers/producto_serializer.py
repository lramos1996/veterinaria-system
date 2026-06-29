from rest_framework import serializers

from inventario.models.productos import (
    Producto
)


class ProductoSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Producto

        fields = "__all__"

    def validate_stock_actual(
        self,
        value
    ):

        if value < 0:

            raise serializers.ValidationError(
                "El stock no puede ser negativo"
            )

        return value

    def validate_stock_minimo(
        self,
        value
    ):

        if value < 0:

            raise serializers.ValidationError(
                "El stock mínimo no puede ser negativo"
            )

        return value

    def validate_costo(
        self,
        value
    ):

        if value < 0:

            raise serializers.ValidationError(
                "El costo no puede ser negativo"
            )

        return value

    def validate_precio_venta(
        self,
        value
    ):

        if value < 0:

            raise serializers.ValidationError(
                "El precio de venta no puede ser negativo"
            )

        return value