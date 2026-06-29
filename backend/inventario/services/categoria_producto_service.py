# inventario/services/categoria_producto_service.py

from inventario.repositories.categoria_producto_repository import (
    CategoriaProductoRepository
)

from shared.exceptions.business_exception import (
    BusinessException
)


class CategoriaProductoService:

    @staticmethod
    def listar():

        return CategoriaProductoRepository.listar()

    @staticmethod
    def obtener(
        categoria_id
    ):

        try:

            return CategoriaProductoRepository.obtener(
                categoria_id
            )

        except Exception:

            raise BusinessException(
                "Categoría no encontrada"
            )

    @staticmethod
    def crear(
        datos
    ):

        if CategoriaProductoRepository.existe_nombre(
            datos["nombre"]
        ):

            raise BusinessException(
                "La categoría ya existe"
            )

        return CategoriaProductoRepository.crear(
            **datos
        )

    @staticmethod
    def actualizar(
        categoria_id,
        datos
    ):

        categoria = (
            CategoriaProductoService.obtener(
                categoria_id
            )
        )

        return (
            CategoriaProductoRepository.actualizar(
                categoria,
                datos
            )
        )

    @staticmethod
    def eliminar(
        categoria_id
    ):

        categoria = (
            CategoriaProductoService.obtener(
                categoria_id
            )
        )

        CategoriaProductoRepository.eliminar(
            categoria
        )