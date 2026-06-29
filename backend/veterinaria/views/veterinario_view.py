from shared.views.crud_view import (
    CrudViewSet
)
from veterinaria.services.veterinario_service import (
    VeterinarioService
)

from veterinaria.serializers.veterinario_serializer import (
    VeterinarioSerializer
)

from rest_framework.response import Response

class VeterinarioViewSet(
    CrudViewSet
):

    service = VeterinarioService

    serializer_class = VeterinarioSerializer

    def list(
        self,
        request
    ):

        especialidad = request.query_params.get(
            "especialidad"
        )

        activo = request.query_params.get(
            "activo"
        )

        if activo is not None:

            activo = (
                activo.lower() == "true"
            )

        if (
            especialidad or
            activo is not None
        ):

            veterinarios = self.service.buscar(
                especialidad,
                activo
            )

        else:

            veterinarios = self.service.listar()

        serializer = self.serializer_class(
            veterinarios,
            many=True
        )

        return Response(
            serializer.data
        )