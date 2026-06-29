from rest_framework import status

from rest_framework.response import (
    Response
)

from rest_framework.viewsets import (
    ViewSet
)

from inventario.services.compra_service import (
    CompraService
)

from inventario.serializers.compra_serializer import (
    CompraSerializer
)

from inventario.serializers.compra_crear_serializer import (
    CompraCrearSerializer
)

from inventario.serializers.compra_detalle_serializer import (
    CompraDetalleSerializer
)

class CompraViewSet(
    ViewSet
):

    def list(
        self,
        request
    ):

        compras = (
            CompraService.listar()
        )

        serializer = (
            CompraSerializer(
                compras,
                many=True
            )
        )

        return Response(
            serializer.data
        )

    def retrieve(
        self,
        request,
        pk=None
    ):

        compra = (
            CompraService.obtener(
                pk
            )
        )

        serializer = (
            CompraDetalleSerializer(
                compra
            )
        )

        return Response(
            serializer.data
        )

    def create(
        self,
        request
    ):

        serializer = (
            CompraCrearSerializer(
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        compra = (
            CompraService.crear(
                serializer.validated_data
            )
        )

        serializer = (
            CompraSerializer(
                compra
            )
        )

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )