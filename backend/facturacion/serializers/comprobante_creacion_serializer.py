from rest_framework import serializers


class ComprobanteCreacionSerializer(
    serializers.Serializer
):

    tipo = serializers.IntegerField()
    orden_servicio = serializers.IntegerField()
    serie = serializers.CharField(
        max_length=10
    )
    numero = serializers.CharField(
        max_length=20
    )
    metodo_pago = serializers.IntegerField()