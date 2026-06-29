from rest_framework import serializers

from inventario.models.detalle_compra import (
    DetalleCompra
)


class DetalleCompraSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = DetalleCompra

        fields = "__all__"