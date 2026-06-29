from rest_framework import serializers

from inventario.models.kardex import (
    Kardex
)


class KardexSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Kardex

        fields = "__all__"