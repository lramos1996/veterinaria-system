from inventario.models.detalle_compra import (
    DetalleCompra
)


class DetalleCompraRepository:

    @staticmethod
    def crear(
        **datos
    ):

        return (
            DetalleCompra.objects.create(
                **datos
            )
        )

    @staticmethod
    def listar_por_producto(
        producto_id
    ):

        return (
            DetalleCompra.objects.filter(
                producto_id=producto_id
            )
            .select_related(
                "compra",
                "compra__proveedor",
                "producto"
            )
            .order_by(
                "-compra__fecha"
            )
        )