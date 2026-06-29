from rest_framework import serializers


class DetalleCompraCrearSerializer(
    serializers.Serializer
):

    producto = serializers.IntegerField()

    cantidad = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    costo_unitario = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )


class CompraCrearSerializer(
    serializers.Serializer
):

    proveedor = serializers.IntegerField()

    numero_documento = serializers.CharField()

    observacion = serializers.CharField(
        required=False,
        allow_blank=True
    )

    detalles = (
        DetalleCompraCrearSerializer(
            many=True
        )
    )