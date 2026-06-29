from inventario.models.movimientos import (
    MovimientoInventario
)


class MovimientoInventarioRepository:

    @staticmethod
    def listar():

        return (
            MovimientoInventario.objects
            .select_related("producto")
            .all()
        )

    @staticmethod
    def obtener(
        movimiento_id
    ):

        return MovimientoInventario.objects.get(
            id=movimiento_id
        )

    @staticmethod
    def crear(
        **datos
    ):

        return MovimientoInventario.objects.create(
            **datos
        )