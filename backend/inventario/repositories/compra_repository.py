from inventario.models.compras import (
    Compra
)


class CompraRepository:

    @staticmethod
    def listar():

        return Compra.objects.all()

    @staticmethod
    def obtener(
        compra_id
    ):

        return Compra.objects.get(
            id=compra_id
        )

    @staticmethod
    def crear(
        **datos
    ):

        return Compra.objects.create(
            **datos
        )
    
    @staticmethod
    def listar_por_proveedor(
        proveedor_id
    ):

        return (
            Compra.objects.filter(
                proveedor_id=proveedor_id
            )
            .order_by("-fecha")
        )
    
    @staticmethod
    def listar_por_producto(
        producto_id
    ):

        return (
            Compra.objects.filter(
                detalles__producto_id=producto_id
            )
            .distinct()
            .order_by("-fecha")
        )