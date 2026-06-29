from inventario.repositories.proveedor_repository import (
    ProveedorRepository
)

from shared.exceptions.business_exception import (
    BusinessException
)


class ProveedorService:

    @staticmethod
    def listar():

        return (
            ProveedorRepository.listar()
        )

    @staticmethod
    def obtener(
        proveedor_id
    ):

        try:

            return (
                ProveedorRepository.obtener(
                    proveedor_id
                )
            )

        except Exception:

            raise BusinessException(
                "Proveedor no encontrado"
            )

    @staticmethod
    def crear(
        datos
    ):

        if ProveedorRepository.existe_ruc(
            datos["ruc"]
        ):

            raise BusinessException(
                "El RUC ya se encuentra registrado"
            )

        return (
            ProveedorRepository.crear(
                **datos
            )
        )

    @staticmethod
    def actualizar(
        proveedor_id,
        datos
    ):

        proveedor = (
            ProveedorService.obtener(
                proveedor_id
            )
        )

        return (
            ProveedorRepository.actualizar(
                proveedor,
                datos
            )
        )

    @staticmethod
    def eliminar(
        proveedor_id
    ):

        proveedor = (
            ProveedorService.obtener(
                proveedor_id
            )
        )

        ProveedorRepository.eliminar(
            proveedor
        )