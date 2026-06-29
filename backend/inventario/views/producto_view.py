from rest_framework.decorators import (
    action
)

from rest_framework.response import (
    Response
)

from shared.views.crud_view import (
    CrudViewSet
)

from inventario.services.producto_service import (
    ProductoService
)

from inventario.serializers.producto_serializer import (
    ProductoSerializer
)

from inventario.services.kardex_service import (
    KardexService
)

from inventario.serializers.kardex_serializers import (
    KardexSerializer
)

from inventario.services.compra_service import (
    CompraService
)

from inventario.serializers.producto_compra_serializer import (
    ProductoCompraSerializer
)

from inventario.serializers.stock_bajo_serializer import (
    StockBajoSerializer
)

from inventario.serializers.reposicion_serializer import (
    ReposicionSerializer
)

class ProductoViewSet(
    CrudViewSet
):

    service = (
        ProductoService
    )

    serializer_class = (
        ProductoSerializer
    )

    @action(
        detail=False,
        methods=["get"]
    )
    def stock_bajo(
        self,
        request
    ):

        productos = (
            self.service.stock_bajo()
        )

        serializer = (
            StockBajoSerializer(
                productos,
                many=True
            )
        )

        return Response(
            serializer.data
        )
    
    @action(
        detail=True,
        methods=["get"]
    )
    def kardex(
        self,
        request,
        pk=None
    ):

        registros = (
            KardexService
            .listar_por_producto(
                pk
            )
        )

        serializer = (
            KardexSerializer(
                registros,
                many=True
            )
        )

        return Response(
            serializer.data
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
            .listar_por_producto(
                pk
            )
        )

        serializer = (
            ProductoCompraSerializer(
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
    def reposicion(
        self,
        request
    ):

        productos = (
            self.service.reposicion()
        )

        serializer = (
            ReposicionSerializer(
                productos,
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