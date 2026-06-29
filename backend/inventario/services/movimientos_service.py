from inventario.models.productos import (
    Producto
)

from inventario.repositories.movimientos_repository import (
    MovimientoInventarioRepository
)

from shared.exceptions.business_exception import (
    BusinessException
)

from inventario.repositories.kardex_repository import (
    KardexRepository
)

class MovimientoInventarioService:

    @staticmethod
    def listar():

        return (
            MovimientoInventarioRepository.listar()
        )

    @staticmethod
    def obtener(
        movimiento_id
    ):

        try:

            return (
                MovimientoInventarioRepository.obtener(
                    movimiento_id
                )
            )

        except Exception:

            raise BusinessException(
                "Movimiento no encontrado"
            )

    @staticmethod
    def crear(
        datos
    ):

        producto = Producto.objects.get(
            id=datos["producto"].id
        )

        stock_anterior = (
            producto.stock_actual
        )

        cantidad = datos["cantidad"]

        tipo = datos["tipo"]

        if tipo == "ENTRADA":

            producto.stock_actual += cantidad

        elif tipo == "SALIDA":

            if producto.stock_actual < cantidad:

                raise BusinessException(
                    f"Stock insuficiente para el producto {producto.nombre}"
                )

            producto.stock_actual -= cantidad

        elif tipo == "AJUSTE":

            producto.stock_actual = cantidad

        producto.save()

        stock_nuevo = (
            producto.stock_actual
        )

        movimiento = (
            MovimientoInventarioRepository.crear(
                **datos
            )
        )

        KardexRepository.crear(
            producto=producto,
            tipo_movimiento=tipo,
            cantidad=cantidad,
            stock_anterior=stock_anterior,
            stock_nuevo=stock_nuevo,
            referencia=datos.get(
                "observacion",
                ""
            )
        )
        return movimiento

    @staticmethod
    def actualizar(
        movimiento_id,
        datos
    ):

        raise BusinessException(
            "Los movimientos de inventario no pueden modificarse"
        )

    @staticmethod
    def eliminar(
        movimiento_id
    ):

        raise BusinessException(
            "Los movimientos de inventario no pueden eliminarse"
        )