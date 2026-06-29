from facturacion.repositories.tipo_comprobante_repository import (
    TipoComprobanteRepository
)

from shared.exceptions.business_exception import (
    BusinessException
)


class TipoComprobanteService:

    @staticmethod
    def listar():

        return (
            TipoComprobanteRepository.listar()
        )

    @staticmethod
    def obtener(
        tipo_id
    ):

        try:

            return (
                TipoComprobanteRepository.obtener(
                    tipo_id
                )
            )

        except Exception:

            raise BusinessException(
                "Tipo de comprobante no encontrado"
            )

    @staticmethod
    def crear(
        datos
    ):

        return (
            TipoComprobanteRepository.crear(
                **datos
            )
        )

    @staticmethod
    def actualizar(
        tipo_id,
        datos
    ):

        tipo = (
            TipoComprobanteRepository.obtener(
                tipo_id
            )
        )

        return (
            TipoComprobanteRepository.actualizar(
                tipo,
                datos
            )
        )

    @staticmethod
    def eliminar(
        tipo_id
    ):

        tipo = (
            TipoComprobanteRepository.obtener(
                tipo_id
            )
        )

        TipoComprobanteRepository.eliminar(
            tipo
        )