from shared.views.crud_view import (
    CrudViewSet
)


from veterinaria.services.historia_clinica_service import (
    HistoriaClinicaService
)

from veterinaria.serializers.historia_clinica_serializer import (
    HistoriaClinicaSerializer
)

from rest_framework.response import Response

class HistoriaClinicaViewSet(
    CrudViewSet
):

    service = HistoriaClinicaService

    serializer_class = HistoriaClinicaSerializer
    
    def list(
        self,
        request
    ):

        mascota = request.query_params.get(
            "mascota"
        )

        veterinario = request.query_params.get(
            "veterinario"
        )

        if (
            mascota or
            veterinario
        ):

            historias = self.service.buscar(
                mascota,
                veterinario
            )

        else:

            historias = self.service.listar()

        serializer = self.serializer_class(
            historias,
            many=True
        )

        return Response(
            serializer.data
        )