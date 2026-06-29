from shared.views.crud_view import (
    CrudViewSet
)

from veterinaria.services.cita_service import (
    CitaService
)

from veterinaria.serializers.cita_serializer import (
    CitaSerializer
)

from rest_framework.response import Response

class CitaViewSet(
    CrudViewSet
):

    service = CitaService

    serializer_class = CitaSerializer

    def list(
        self,
        request
    ):

        fecha = request.query_params.get(
            "fecha"
        )

        veterinario = request.query_params.get(
            "veterinario"
        )

        mascota = request.query_params.get(
            "mascota"
        )

        if (
            fecha or
            veterinario or
            mascota
        ):

            citas = self.service.buscar(
                fecha,
                veterinario,
                mascota
            )

        else:

            citas = self.service.listar()

        serializer = self.serializer_class(
            citas,
            many=True
        )

        return Response(
            serializer.data
        )