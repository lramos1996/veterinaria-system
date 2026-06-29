from shared.views.crud_view import (
    CrudViewSet
)

from veterinaria.services.mascota_service import (
    MascotaService
)

from veterinaria.serializers.mascota_serializer import (
    MascotaSerializer
)

from rest_framework.response import Response

class MascotaViewSet(
    CrudViewSet
):

    service = MascotaService

    serializer_class = MascotaSerializer

    def list(
        self,
        request
    ):

        nombre = request.query_params.get(
            "nombre"
        )

        especie = request.query_params.get(
            "especie"
        )

        propietario = request.query_params.get(
            "propietario"
        )

        if (
            nombre or
            especie or
            propietario
        ):

            mascotas = self.service.buscar(
                nombre,
                especie,
                propietario
            )

        else:

            mascotas = self.service.listar()

        serializer = self.serializer_class(
            mascotas,
            many=True
        )

        return Response(
            serializer.data
        )