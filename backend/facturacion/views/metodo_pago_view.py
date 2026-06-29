from shared.views.crud_view import (
    CrudViewSet
)

from facturacion.services.metodo_pago_service import (
    MetodoPagoService
)

from facturacion.serializers.metodo_pago_serializer import (
    MetodoPagoSerializer
)


class MetodoPagoViewSet(
    CrudViewSet
):

    service = (
        MetodoPagoService
    )

    serializer_class = (
        MetodoPagoSerializer
    )