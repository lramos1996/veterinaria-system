from facturacion.repositories.metodo_pago_repository import (
    MetodoPagoRepository
)

from shared.exceptions.business_exception import (
    BusinessException
)


class MetodoPagoService:

    @staticmethod
    def listar():

        return (
            MetodoPagoRepository.listar()
        )

    @staticmethod
    def obtener(
        metodo_pago_id
    ):

        try:

            return (
                MetodoPagoRepository.obtener(
                    metodo_pago_id
                )
            )

        except Exception:

            raise BusinessException(
                "Método de pago no encontrado"
            )

    @staticmethod
    def crear(
        datos
    ):

        return (
            MetodoPagoRepository.crear(
                **datos
            )
        )

    @staticmethod
    def actualizar(
        metodo_pago_id,
        datos
    ):

        metodo_pago = (
            MetodoPagoRepository.obtener(
                metodo_pago_id
            )
        )

        return (
            MetodoPagoRepository.actualizar(
                metodo_pago,
                datos
            )
        )

    @staticmethod
    def eliminar(
        metodo_pago_id
    ):

        metodo_pago = (
            MetodoPagoRepository.obtener(
                metodo_pago_id
            )
        )

        MetodoPagoRepository.eliminar(
            metodo_pago
        )