from rest_framework import serializers

from veterinaria.models import (
    Veterinario
)


class VeterinarioSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = Veterinario

        fields = "__all__"

        read_only_fields = (
            "id",
            "fecha_creacion"
        )

    def validate_nombres(
        self,
        value
    ):

        if not value.strip():

            raise serializers.ValidationError(
                "Los nombres son obligatorios"
            )

        return value

    def validate_apellidos(
        self,
        value
    ):

        if not value.strip():

            raise serializers.ValidationError(
                "Los apellidos son obligatorios"
            )

        return value

    def validate_colegiatura(
        self,
        value
    ):

        if not value.strip():

            raise serializers.ValidationError(
                "La colegiatura es obligatoria"
            )

        return value