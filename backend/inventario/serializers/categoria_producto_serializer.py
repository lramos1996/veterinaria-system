# inventario/serializers/categoria_producto_serializer.py

from rest_framework import serializers

from inventario.models.categorias import (
    CategoriaProducto
)



class CategoriaProductoSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = CategoriaProducto

        fields = "__all__"

    def validate_nombre(
        self,
        value
    ):

        if not value.strip():

            raise serializers.ValidationError(
                "El nombre es obligatorio"
            )

        return value