from decimal import Decimal

from facturacion.repositories.orden_servicio_repository import (
    OrdenServicioRepository
)

from facturacion.repositories.detalle_orden_servicio_repository import (
    DetalleOrdenServicioRepository
)

from shared.exceptions.business_exception import (
    BusinessException
)


class OrdenServicioService:

    @staticmethod
    def listar():

        return (
            OrdenServicioRepository.listar()
        )

    @staticmethod
    def obtener(
        orden_id
    ):

        try:

            return (
                OrdenServicioRepository.obtener(
                    orden_id
                )
            )

        except Exception:

            raise BusinessException(
                "Orden de servicio no encontrada"
            )

    @staticmethod
    def crear(
        datos
    ):

        return (
            OrdenServicioRepository.crear(
                **datos
            )
        )

    @staticmethod
    def actualizar(
        orden_id,
        datos
    ):

        orden = (
            OrdenServicioService.obtener(
                orden_id
            )
        )

        if orden.estado == "FACTURADA":

            raise BusinessException(
                "No se puede modificar una orden facturada"
            )

        return (
            OrdenServicioRepository.actualizar(
                orden,
                datos
            )
        )

    @staticmethod
    def eliminar(
        orden_id
    ):

        orden = (
            OrdenServicioService.obtener(
                orden_id
            )
        )

        if orden.estado == "FACTURADA":

            raise BusinessException(
                "No se puede eliminar una orden facturada"
            )

        OrdenServicioRepository.eliminar(
            orden
        )

    @staticmethod
    def recalcular_total(
        orden_id
    ):

        orden = (
            OrdenServicioService.obtener(
                orden_id
            )
        )

        detalles = (
            DetalleOrdenServicioRepository
            .listar_por_orden(
                orden_id
            )
        )

        total = sum(
            detalle.subtotal
            for detalle in detalles
        )

        orden.total = total or Decimal("0.00")
        orden.save()

        return orden