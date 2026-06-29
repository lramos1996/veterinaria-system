from rest_framework import serializers

from veterinaria.models.clientes import Cliente


class ClienteSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Cliente

        fields = "__all__"

        read_only_fields = (
            "id",
            "fecha_creacion"
        )

    def validate_documento(
        self,
        value
    ):

        value = value.strip()

        if not value:

            raise serializers.ValidationError(
                "El documento es obligatorio"
            )

        if not value.isdigit():

            raise serializers.ValidationError(
                "El documento solo debe contener números"
            )

        if len(value) != 8:

            raise serializers.ValidationError(
                "El documento debe tener 8 dígitos"
            )

        return value

    def validate_telefono(
        self,
        value
    ):

        value = value.strip()

        if not value:

            raise serializers.ValidationError(
                "El teléfono es obligatorio"
            )

        if not value.isdigit():

            raise serializers.ValidationError(
                "El teléfono solo debe contener números"
            )

        if len(value) < 9:

            raise serializers.ValidationError(
                "El teléfono debe tener al menos 9 dígitos"
            )

        return value

    def validate_nombres(
        self,
        value
    ):

        value = value.strip()

        if not value:

            raise serializers.ValidationError(
                "Los nombres son obligatorios"
            )

        return value

    def validate_apellidos(
        self,
        value
    ):

        value = value.strip()

        if not value:

            raise serializers.ValidationError(
                "Los apellidos son obligatorios"
            )

        return value