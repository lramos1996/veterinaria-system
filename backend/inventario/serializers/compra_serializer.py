from rest_framework import serializers

from inventario.models.compras import (
    Compra
)


class CompraSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Compra

        fields = "__all__"