from rest_framework.response import Response

from shared.views.crud_view import (
    CrudViewSet
)

from veterinaria.services.cliente_service import (
    ClienteService
)

from veterinaria.serializers.cliente_serializer import (
    ClienteSerializer
)


class ClienteViewSet(
    CrudViewSet
):

    service = ClienteService

    serializer_class = ClienteSerializer

    def list(
        self,
        request
    ):

        documento = request.query_params.get(
            "documento"
        )

        nombre = request.query_params.get(
            "nombre"
        )

        if documento or nombre:

            clientes = self.service.buscar(
                documento=documento,
                nombre=nombre
            )

        else:

            clientes = self.service.listar()

        serializer = self.serializer_class(
            clientes,
            many=True
        )

        return Response(
            serializer.data
        )