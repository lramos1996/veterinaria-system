from veterinaria.models.citas import Cita


class CitaRepository:

    @staticmethod
    def listar():
        return (
            Cita.objects
            .select_related(
                "mascota",
                "veterinario"
            )
            .all()
        )

    @staticmethod
    def obtener(cita_id):
        return Cita.objects.get(
            id=cita_id
        )

    @staticmethod
    def crear(**datos):

        return Cita.objects.create(
            mascota_id=datos["mascota"],
            veterinario_id=datos["veterinario"],
            fecha=datos["fecha"],
            hora=datos["hora"],
            motivo=datos["motivo"],
            estado=datos.get(
                "estado",
                "PROGRAMADA"
            ),
            observaciones=datos.get(
                "observaciones",
                ""
            )
        )

    @staticmethod
    def actualizar(cita, datos):

        for campo, valor in datos.items():
            setattr(
                cita,
                campo,
                valor
            )

        cita.save()

        return cita

    @staticmethod
    def eliminar(cita):
        cita.delete()

    @staticmethod
    def existe_conflicto(
        veterinario_id,
        fecha,
        hora
    ):

        return Cita.objects.filter(
            veterinario_id=veterinario_id,
            fecha=fecha,
            hora=hora,
            estado="PROGRAMADA"
        ).exists()

    @staticmethod
    def buscar(
        fecha=None,
        veterinario=None,
        mascota=None
    ):

        queryset = Cita.objects.all()

        if fecha:

            queryset = queryset.filter(
                fecha=fecha
            )

        if veterinario:

            queryset = queryset.filter(
                veterinario_id=veterinario
            )

        if mascota:

            queryset = queryset.filter(
                mascota_id=mascota
            )

        return queryset