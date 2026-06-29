from rest_framework import serializers

from inventario.models.detalle_compra import (
    DetalleCompra
)


class ProductoCompraSerializer(
    serializers.ModelSerializer
):

    compra_id = serializers.IntegerField(
        source="compra.id"
    )

    fecha = serializers.DateTimeField(
        source="compra.fecha"
    )

    proveedor = serializers.CharField(
        source="compra.proveedor.razon_social"
    )

    numero_documento = serializers.CharField(
        source="compra.numero_documento"
    )

    class Meta:

        model = DetalleCompra

        fields = [
            "compra_id",
            "fecha",
            "proveedor",
            "numero_documento",
            "cantidad",
            "costo_unitario",
            "subtotal"
        ]