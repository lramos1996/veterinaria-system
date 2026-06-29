from inventario.repositories.producto_repository import (
    ProductoRepository
)

from shared.exceptions.business_exception import (
    BusinessException
)


class ProductoService:

    @staticmethod
    def listar():

        return ProductoRepository.listar()

    @staticmethod
    def obtener(
        producto_id
    ):

        try:

            return ProductoRepository.obtener(
                producto_id
            )

        except Exception:

            raise BusinessException(
                "Producto no encontrado"
            )

    @staticmethod
    def crear(
        datos
    ):

        if ProductoRepository.existe_codigo(
            datos["codigo"]
        ):

            raise BusinessException(
                "El código ya existe"
            )

        return ProductoRepository.crear(
            **datos
        )

    @staticmethod
    def actualizar(
        producto_id,
        datos
    ):

        producto = ProductoService.obtener(
            producto_id
        )

        return ProductoRepository.actualizar(
            producto,
            datos
        )

    @staticmethod
    def eliminar(
        producto_id
    ):

        producto = ProductoService.obtener(
            producto_id
        )

        ProductoRepository.eliminar(
            producto
        )

    @staticmethod
    def stock_bajo():

        return ProductoRepository.stock_bajo()
    
    @staticmethod
    def dashboard():

        return (
            ProductoRepository.dashboard()
        )
    
    @staticmethod
    def reposicion():

        return (
            ProductoRepository.reposicion()
        )