from inventario.models.kardex import (
    Kardex
)


class KardexRepository:

    @staticmethod
    def listar():

        return (
            Kardex.objects
            .select_related("producto")
            .all()
        )

    @staticmethod
    def obtener(
        kardex_id
    ):

        return Kardex.objects.get(
            id=kardex_id
        )

    @staticmethod
    def crear(
        **datos
    ):

        return Kardex.objects.create(
            **datos
        )

    @staticmethod
    def listar_por_producto(
        producto_id
    ):

        return (
            Kardex.objects
            .filter(
                producto_id=producto_id
            )
            .order_by("-fecha")
        )