from rest_framework import serializers


class ComprobanteDashboardSerializer(
    serializers.Serializer
):

    cantidad_comprobantes = serializers.IntegerField()

    subtotal_total = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    igv_total = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    ventas_total = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    ticket_promedio = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )