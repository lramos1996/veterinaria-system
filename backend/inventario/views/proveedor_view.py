from shared.views.crud_view import (
    CrudViewSet
)

from inventario.services.proveedor_service import (
    ProveedorService
)

from inventario.serializers.proveedor_serializer import (
    ProveedorSerializer
)

from rest_framework.decorators import (
    action
)

from rest_framework.response import (
    Response
)

from inventario.services.compra_service import (
    CompraService
)

from inventario.serializers.compra_serializer import (
    CompraSerializer
)

class ProveedorViewSet(
    CrudViewSet
):

    service = (
        ProveedorService
    )

    serializer_class = (
        ProveedorSerializer
    )
        
    @action(
        detail=True,
        methods=["get"]
    )
    def compras(
        self,
        request,
        pk=None
    ):

        compras = (
            CompraService
            .listar_por_proveedor(
                pk
            )
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
    
    @action(
        detail=False,
        methods=["get"]
    )
    def dashboard(
        self,
        request
    ):

        return Response(
            self.service.dashboard()
        )
    
