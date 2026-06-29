from decimal import Decimal

from facturacion.models.comprobantes import (
    Comprobante
)

from facturacion.models.pagos import (
    MetodoPago
)

from facturacion.repositories.movimiento_caja_repository import (
    MovimientoCajaRepository
)

from shared.exceptions.business_exception import (
    BusinessException
)


class MovimientoCajaService:

    @staticmethod
    def listar():

        return (
            MovimientoCajaRepository.listar()
        )

    @staticmethod
    def obtener(
        movimiento_id
    ):

        try:

            return (
                MovimientoCajaRepository.obtener(
                    movimiento_id
                )
            )

        except Exception:

            raise BusinessException(
                "Movimiento de caja no encontrado"
            )

    @staticmethod
    def crear(
        datos
    ):

        comprobante = None

        if datos.get("comprobante"):

            try:

                comprobante = Comprobante.objects.get(
                    id=datos["comprobante"].id
                )

            except Comprobante.DoesNotExist:

                raise BusinessException(
                    "Comprobante no encontrado"
                )

        try:

            metodo_pago = MetodoPago.objects.get(
                id=datos["metodo_pago"].id
            )

        except MetodoPago.DoesNotExist:

            raise BusinessException(
                "Método de pago no encontrado"
            )

        tipo = datos["tipo"]
        monto = datos["monto"]

        if tipo not in ["INGRESO", "EGRESO"]:

            raise BusinessException(
                "Tipo de movimiento inválido"
            )

        if Decimal(monto) <= 0:

            raise BusinessException(
                "El monto debe ser mayor a 0"
            )

        return (
            MovimientoCajaRepository.crear(
                comprobante=comprobante,
                metodo_pago=metodo_pago,
                tipo=tipo,
                monto=monto,
                observacion=datos.get(
                    "observacion",
                    ""
                )
            )
        )

    @staticmethod
    def actualizar(
        movimiento_id,
        datos
    ):

        raise BusinessException(
            "Los movimientos de caja no pueden modificarse"
        )

    @staticmethod
    def eliminar(
        movimiento_id
    ):

        raise BusinessException(
            "Los movimientos de caja no pueden eliminarse"
        )

    @staticmethod
    def dashboard():

        ingresos = Decimal(
            MovimientoCajaRepository.ingresos_total()
        )

        egresos = Decimal(
            MovimientoCajaRepository.egresos_total()
        )

        saldo = ingresos - egresos

        movimientos = (
            MovimientoCajaRepository.listar()
        )

        return {
            "ingresos": ingresos,
            "egresos": egresos,
            "saldo": saldo,
            "cantidad_movimientos": movimientos.count()
        }

    @staticmethod
    def ultimos_movimientos(
        limite=10
    ):

        return (
            MovimientoCajaRepository.ultimos_movimientos(
                limite
            )
        )