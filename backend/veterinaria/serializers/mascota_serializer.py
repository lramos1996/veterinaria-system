from datetime import date

from rest_framework import serializers

from veterinaria.models.mascotas import (
    Mascota
)


class MascotaSerializer(
    serializers.ModelSerializer
):

    nombre_propietario = (
        serializers.SerializerMethodField()
    )

    class Meta:

        model = Mascota

        fields = [
            "id",
            "nombre",
            "especie",
            "raza",
            "sexo",
            "fecha_nacimiento",
            "peso",
            "color",
            "observaciones",
            "propietario",
            "nombre_propietario"
        ]

        read_only_fields = (
            "id",
            "nombre_propietario"
        )

    def validate_nombre(
        self,
        value
    ):

        value = value.strip()

        if not value:

            raise serializers.ValidationError(
                "El nombre es obligatorio"
            )

        return value

    def validate_fecha_nacimiento(
        self,
        value
    ):

        if value and value > date.today():

            raise serializers.ValidationError(
                "La fecha de nacimiento no puede ser futura"
            )

        return value

    def validate_peso(
        self,
        value
    ):

        if value is not None and value <= 0:

            raise serializers.ValidationError(
                "El peso debe ser mayor a cero"
            )

        return value

    def get_nombre_propietario(
        self,
        obj
    ):

        return (
            f"{obj.propietario.nombres} "
            f"{obj.propietario.apellidos}"
        )