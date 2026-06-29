from shared.views.crud_view import (
    CrudViewSet
)

from inventario.services.kardex_service import (
    KardexService
)

from inventario.serializers.kardex_serializers import (
    KardexSerializer
)


class KardexViewSet(
    CrudViewSet
):

    service = KardexService

    serializer_class = KardexSerializer