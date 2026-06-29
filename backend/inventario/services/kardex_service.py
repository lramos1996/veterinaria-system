from inventario.repositories.kardex_repository import (
    KardexRepository
)

from shared.exceptions.business_exception import (
    BusinessException
)


class KardexService:

    @staticmethod
    def listar():

        return (
            KardexRepository.listar()
        )

    @staticmethod
    def obtener(
        kardex_id
    ):

        try:

            return (
                KardexRepository.obtener(
                    kardex_id
                )
            )

        except Exception:

            raise BusinessException(
                "Registro kardex no encontrado"
            )

    @staticmethod
    def listar_por_producto(
        producto_id
    ):

        return (
            KardexRepository
            .listar_por_producto(
                producto_id
            )
        )

    @staticmethod
    def crear(
        datos
    ):

        raise BusinessException(
            "El kardex se genera automáticamente"
        )


    @staticmethod
    def actualizar(
        kardex_id,
        datos
    ):

        raise BusinessException(
            "No se puede modificar el kardex"
        )


    @staticmethod
    def eliminar(
        kardex_id
    ):

        raise BusinessException(
            "No se puede eliminar el kardex"
        )