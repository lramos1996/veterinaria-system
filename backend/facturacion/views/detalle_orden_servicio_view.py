from shared.views.crud_view import (
    CrudViewSet
)

from facturacion.services.detalle_orden_servicio_service import (
    DetalleOrdenServicioService
)

from facturacion.serializers.detalle_orden_servicio_serializer import (
    DetalleOrdenServicioSerializer
)


class DetalleOrdenServicioViewSet(
    CrudViewSet
):

    service = (
        DetalleOrdenServicioService
    )

    serializer_class = (
        DetalleOrdenServicioSerializer
    )