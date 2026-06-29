from shared.views.crud_view import (
    CrudViewSet
)

from inventario.services.movimientos_service import (
    MovimientoInventarioService
)

from inventario.serializers.movimientos_serializer import (
    MovimientoInventarioSerializer
)


class MovimientoInventarioViewSet(
    CrudViewSet
):

    service = MovimientoInventarioService

    serializer_class = MovimientoInventarioSerializer

    