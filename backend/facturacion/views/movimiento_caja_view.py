from rest_framework.decorators import (
    action
)

from rest_framework.response import (
    Response
)

from shared.views.crud_view import (
    CrudViewSet
)

from facturacion.services.movimiento_caja_service import (
    MovimientoCajaService
)

from facturacion.serializers.movimiento_caja_serializer import (
    MovimientoCajaSerializer
)

from facturacion.serializers.movimiento_caja_dashboard_serializer import (
    MovimientoCajaDashboardSerializer
)


class MovimientoCajaViewSet(
    CrudViewSet
):

    service = (
        MovimientoCajaService
    )

    serializer_class = (
        MovimientoCajaSerializer
    )

    @action(
        detail=False,
        methods=["get"]
    )
    def dashboard(
        self,
        request
    ):

        data = self.service.dashboard()

        serializer = (
            MovimientoCajaDashboardSerializer(
                data
            )
        )

        return Response(
            serializer.data
        )

    @action(
        detail=False,
        methods=["get"]
    )
    def recientes(
        self,
        request
    ):

        movimientos = (
            self.service.ultimos_movimientos()
        )

        serializer = (
            self.serializer_class(
                movimientos,
                many=True
            )
        )

        return Response(
            serializer.data
        )