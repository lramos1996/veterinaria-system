from shared.views.crud_view import (
    CrudViewSet
)

from facturacion.services.tipo_comprobante_service import (
    TipoComprobanteService
)

from facturacion.serializers.tipo_comprobante_serializer import (
    TipoComprobanteSerializer
)


class TipoComprobanteViewSet(
    CrudViewSet
):

    service = (
        TipoComprobanteService
    )

    serializer_class = (
        TipoComprobanteSerializer
    )