from decimal import Decimal
from django.db import transaction
from datetime import datetime
from facturacion.models.tipos_comprobante import (
    TipoComprobante
)

from facturacion.models.pagos import (
    MetodoPago
)

from facturacion.repositories.comprobante_repository import (
    ComprobanteRepository
)

from facturacion.repositories.detalle_comprobante_repository import (
    DetalleComprobanteRepository
)

from facturacion.repositories.movimiento_caja_repository import (
    MovimientoCajaRepository
)

from facturacion.services.orden_servicio_service import (
    OrdenServicioService
)

from facturacion.repositories.detalle_orden_servicio_repository import (
    DetalleOrdenServicioRepository
)

from inventario.services.movimientos_service import (
    MovimientoInventarioService
)

from shared.exceptions.business_exception import (
    BusinessException
)


class ComprobanteService:

    IGV_PORCENTAJE = Decimal("0.18")

    @staticmethod
    def listar():

        return (
            ComprobanteRepository.listar()
        )

    @staticmethod
    def obtener(
        comprobante_id
    ):

        try:

            return (
                ComprobanteRepository.obtener(
                    comprobante_id
                )
            )

        except Exception:

            raise BusinessException(
                "Comprobante no encontrado"
            )

    @staticmethod
    @transaction.atomic
    def crear(
        datos
    ):

        tipo_id = datos["tipo"]
        orden_id = datos["orden_servicio"]
        metodo_pago_id = datos["metodo_pago"]
        serie = datos["serie"]
        numero = datos["numero"]

        if ComprobanteRepository.existe_serie_numero(
            serie,
            numero
        ):

            raise BusinessException(
                "Ya existe un comprobante con esa serie y número"
            )

        try:

            tipo = TipoComprobante.objects.get(
                id=tipo_id
            )

        except TipoComprobante.DoesNotExist:

            raise BusinessException(
                "Tipo de comprobante no encontrado"
            )

        try:

            metodo_pago = MetodoPago.objects.get(
                id=metodo_pago_id
            )

        except MetodoPago.DoesNotExist:

            raise BusinessException(
                "Método de pago no encontrado"
            )

        orden = OrdenServicioService.obtener(
            orden_id
        )

        if orden.estado == "FACTURADA":

            raise BusinessException(
                "La orden ya fue facturada"
            )

        detalles_orden = (
            DetalleOrdenServicioRepository
            .listar_por_orden(
                orden.id
            )
        )

        if not detalles_orden.exists():

            raise BusinessException(
                "La orden no tiene detalles"
            )

        subtotal = sum(
            detalle.subtotal
            for detalle in detalles_orden
        )

        subtotal = Decimal(subtotal).quantize(
            Decimal("0.01")
        )

        igv = (
            subtotal * ComprobanteService.IGV_PORCENTAJE
        ).quantize(
            Decimal("0.01")
        )

        total = (
            subtotal + igv
        ).quantize(
            Decimal("0.01")
        )

        comprobante = (
            ComprobanteRepository.crear(
                tipo=tipo,
                orden_servicio=orden,
                serie=serie,
                numero=numero,
                subtotal=subtotal,
                igv=igv,
                total=total
            )
        )

        for detalle in detalles_orden:

            DetalleComprobanteRepository.crear(
                comprobante=comprobante,
                producto=detalle.producto,
                descripcion=detalle.descripcion,
                cantidad=detalle.cantidad,
                precio_unitario=detalle.precio_unitario,
                subtotal=detalle.subtotal
            )

            if detalle.producto:

                MovimientoInventarioService.crear(
                    {
                        "producto": detalle.producto,
                        "tipo": "SALIDA",
                        "cantidad": detalle.cantidad,
                        "observacion": (
                            f"Venta comprobante "
                            f"{serie}-{numero}"
                        )
                    }
                )

        MovimientoCajaRepository.crear(
            comprobante=comprobante,
            metodo_pago=metodo_pago,
            tipo="INGRESO",
            monto=total,
            observacion=(
                f"Pago de comprobante "
                f"{serie}-{numero}"
            )
        )

        orden.estado = "FACTURADA"
        orden.save()

        return comprobante

    @staticmethod
    def actualizar(
        comprobante_id,
        datos
    ):

        raise BusinessException(
            "Los comprobantes no pueden modificarse"
        )

    @staticmethod
    def eliminar(
        comprobante_id
    ):

        raise BusinessException(
            "Los comprobantes no pueden eliminarse"
        )
    
    @staticmethod
    def dashboard():

        return (
            ComprobanteRepository.dashboard()
        )

    @staticmethod
    def listar_por_fecha(
        desde,
        hasta
    ):
       
        try:

            desde_date = datetime.strptime(
                desde,
                "%Y-%m-%d"
            ).date()

            hasta_date = datetime.strptime(
                hasta,
                "%Y-%m-%d"
            ).date()

        except ValueError:

            raise BusinessException(
                "Formato de fecha inválido. Usa YYYY-MM-DD"
            )

        if desde_date > hasta_date:

            raise BusinessException(
                "La fecha desde no puede ser mayor que hasta"
            )

        return (
            ComprobanteRepository.listar_por_fecha(
                desde_date,
                hasta_date
            )
        )

    @staticmethod
    def recientes():

        return (
            ComprobanteRepository.recientes()
        )

    @staticmethod
    def productos_mas_vendidos():

        return (
            ComprobanteRepository.productos_mas_vendidos()
        )

    @staticmethod
    def clientes_top():

        return (
            ComprobanteRepository.clientes_top()
        )