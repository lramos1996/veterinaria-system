from rest_framework import serializers


class MovimientoCajaDashboardSerializer(
    serializers.Serializer
):

    ingresos = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    egresos = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    saldo = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    cantidad_movimientos = serializers.IntegerField()