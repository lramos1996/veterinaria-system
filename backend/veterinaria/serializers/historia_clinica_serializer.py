from rest_framework import serializers

from veterinaria.models import (
    HistoriaClinica
)


class HistoriaClinicaSerializer(
    serializers.ModelSerializer
):

    nombre_mascota = (
        serializers.SerializerMethodField()
    )

    nombre_veterinario = (
        serializers.SerializerMethodField()
    )

    class Meta:

        model = HistoriaClinica

        fields = "__all__"

        read_only_fields = (
            "id",
            "fecha_creacion",
            "nombre_mascota",
            "nombre_veterinario"
        )

    def validate_peso(
        self,
        value
    ):

        if value is not None and value <= 0:

            raise serializers.ValidationError(
                "El peso debe ser mayor a cero"
            )

        return value

    def validate_temperatura(
        self,
        value
    ):

        if (
            value is not None and
            (
                value < 30 or
                value > 45
            )
        ):

            raise serializers.ValidationError(
                "Temperatura fuera de rango"
            )

        return value

    def get_nombre_mascota(
        self,
        obj
    ):

        return obj.mascota.nombre

    def get_nombre_veterinario(
        self,
        obj
    ):

        return (
            f"{obj.veterinario.nombres} "
            f"{obj.veterinario.apellidos}"
        )