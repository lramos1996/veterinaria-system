from veterinaria.models import HistoriaClinica


class HistoriaClinicaRepository:

    @staticmethod
    def listar():

        return HistoriaClinica.objects.select_related(
            "mascota",
            "veterinario"
        ).all()

    @staticmethod
    def obtener(id):

        return HistoriaClinica.objects.get(
            pk=id
        )

    @staticmethod
    def crear(**datos):

        return HistoriaClinica.objects.create(
            **datos
        )
    
    @staticmethod
    def actualizar(historial, datos):

        for campo, valor in datos.items():
            setattr(historial, campo, valor)

        historial.save()

        return historial

    @staticmethod
    def eliminar(historial):
        historial.delete()

    @staticmethod
    def buscar(
        mascota=None,
        veterinario=None
    ):

        queryset = (
            HistoriaClinica.objects
            .select_related(
                "mascota",
                "veterinario"
            )
        )

        if mascota:

            queryset = queryset.filter(
                mascota_id=mascota
            )

        if veterinario:

            queryset = queryset.filter(
                veterinario_id=veterinario
            )

        return queryset