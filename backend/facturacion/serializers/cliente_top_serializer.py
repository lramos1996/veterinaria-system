from rest_framework import serializers


class ClienteTopSerializer(
    serializers.Serializer
):

    orden_servicio__cliente = serializers.IntegerField()

    orden_servicio__cliente__nombres = serializers.CharField()
    orden_servicio__cliente__apellidos = serializers.CharField()

    cantidad_comprobantes = serializers.IntegerField()

    total_comprado = serializers.DecimalField(
        max_digits=12,
        decimal_places=2
    )