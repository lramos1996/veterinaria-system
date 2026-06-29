from rest_framework import serializers

from inventario.models.compras import (
    Compra
)

from inventario.serializers.detalle_compra_serializer import (
    DetalleCompraSerializer
)


class CompraDetalleSerializer(
    serializers.ModelSerializer
):

    detalles = (
        DetalleCompraSerializer(
            many=True,
            read_only=True
        )
    )

    class Meta:

        model = Compra

        fields = "__all__"