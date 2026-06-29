from rest_framework import serializers

from inventario.models.productos import (
    Producto
)


class ReposicionSerializer(
    serializers.ModelSerializer
):

    sugerido_comprar = (
        serializers.SerializerMethodField()
    )

    class Meta:

        model = Producto

        fields = [
            "id",
            "codigo",
            "nombre",
            "stock_actual",
            "stock_minimo",
            "sugerido_comprar"
        ]

    def get_sugerido_comprar(
        self,
        obj
    ):

        return (
            obj.stock_minimo * 2
            - obj.stock_actual
        )