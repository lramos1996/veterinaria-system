from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import (
    action
)

from shared.views.crud_view import (
    CrudViewSet
)

from facturacion.services.comprobante_service import (
    ComprobanteService
)

from facturacion.serializers.comprobante_serializer import (
    ComprobanteSerializer
)

from facturacion.serializers.comprobante_creacion_serializer import (
    ComprobanteCreacionSerializer
)

from facturacion.serializers.comprobante_detalle_serializer import (
    ComprobanteDetalleSerializer
)

from facturacion.serializers.comprobante_dashboard_serializer import (
    ComprobanteDashboardSerializer
)

from facturacion.serializers.producto_mas_vendido_serializer import (
    ProductoMasVendidoSerializer
)

from facturacion.serializers.cliente_top_serializer import (
    ClienteTopSerializer
)

class ComprobanteViewSet(
    CrudViewSet
):

    service = (
        ComprobanteService
    )

    serializer_class = (
        ComprobanteSerializer
    )

    def create(
        self,
        request
    ):

        serializer = (
            ComprobanteCreacionSerializer(
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        comprobante = self.service.crear(
            serializer.validated_data
        )

        response_serializer = (
            ComprobanteSerializer(
                comprobante
            )
        )

        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED
        )

    def update(
        self,
        request,
        pk=None
    ):

        return Response(
            {
                "error": "Los comprobantes no pueden modificarse"
            },
            status=status.HTTP_405_METHOD_NOT_ALLOWED
        )

    def destroy(
        self,
        request,
        pk=None
    ):

        return Response(
            {
                "error": "Los comprobantes no pueden eliminarse"
            },
            status=status.HTTP_405_METHOD_NOT_ALLOWED
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

        comprobante = self.service.obtener(
            pk
        )

        serializer = (
            ComprobanteDetalleSerializer(
                comprobante
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

        data = self.service.dashboard()

        serializer = (
            ComprobanteDashboardSerializer(
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
    def por_fecha(
        self,
        request
    ):
         
             
        desde = request.query_params.get(
            "desde"
        )

        hasta = request.query_params.get(
            "hasta"
        )

        if not desde or not hasta:
            return Response(
                {
                    "error": "Debes enviar desde y hasta"
                },
                status=400
            ) 
        
        comprobantes = (
            self.service.listar_por_fecha(
                desde,
                hasta
            )
        )

        serializer = (
            self.serializer_class(
                comprobantes,
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
    def recientes(
        self,
        request
    ):

        comprobantes = (
            self.service.recientes()
        )

        serializer = (
            self.serializer_class(
                comprobantes,
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
    def productos_mas_vendidos(
        self,
        request
    ):

        data = (
            self.service.productos_mas_vendidos()
        )

        serializer = (
            ProductoMasVendidoSerializer(
                data,
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
    def clientes_top(
        self,
        request
    ):

        data = (
            self.service.clientes_top()
        )

        serializer = (
            ClienteTopSerializer(
                data,
                many=True
            )
        )

        return Response(
            serializer.data
        )