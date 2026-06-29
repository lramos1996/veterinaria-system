from rest_framework import serializers


class ProductoMasVendidoSerializer(
    serializers.Serializer
):

    producto = serializers.IntegerField()
    producto__codigo = serializers.CharField()
    producto__nombre = serializers.CharField()

    total_cantidad = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    total_ventas = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )