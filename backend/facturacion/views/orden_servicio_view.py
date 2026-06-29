from rest_framework.decorators import (
    action
)

from rest_framework.response import (
    Response
)

from shared.views.crud_view import (
    CrudViewSet
)

from facturacion.services.orden_servicio_service import (
    OrdenServicioService
)

from facturacion.serializers.orden_servicio_serializer import (
    OrdenServicioSerializer
)

from facturacion.serializers.orden_servicio_detalle_serializer import (
    OrdenServicioDetalleSerializer
)


class OrdenServicioViewSet(
    CrudViewSet
):

    service = (
        OrdenServicioService
    )

    serializer_class = (
        OrdenServicioSerializer
    )

    @action(
        detail=True,
        methods=["get"]
    )
    def detalle(
        self,
        request,
        pk=None
    ):

        orden = self.service.obtener(
            pk
        )

        serializer = (
            OrdenServicioDetalleSerializer(
                orden
            )
        )

        return Response(
            serializer.data
        )