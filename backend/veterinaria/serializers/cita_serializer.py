from datetime import date

from rest_framework import serializers

from veterinaria.models.citas import (
    Cita
)


class CitaSerializer(
    serializers.ModelSerializer
):

    nombre_mascota = (
        serializers.SerializerMethodField()
    )

    nombre_veterinario = (
        serializers.SerializerMethodField()
    )

    class Meta:

        model = Cita

        fields = "__all__"

        read_only_fields = (
            "id",
            "nombre_mascota",
            "nombre_veterinario"
        )

    def validate_fecha(
        self,
        value
    ):

        if value < date.today():

            raise serializers.ValidationError(
                "La fecha no puede ser pasada"
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

        return str(
            obj.veterinario
        )