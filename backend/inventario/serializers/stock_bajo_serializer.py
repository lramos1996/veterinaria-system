from rest_framework import serializers

from inventario.models.productos import (
    Producto
)


class StockBajoSerializer(
    serializers.ModelSerializer
):

    faltante = serializers.SerializerMethodField()

    class Meta:

        model = Producto

        fields = [
            "id",
            "codigo",
            "nombre",
            "stock_actual",
            "stock_minimo",
            "faltante"
        ]

    def get_faltante(
        self,
        obj
    ):

        return (
            obj.stock_minimo
            - obj.stock_actual
        )