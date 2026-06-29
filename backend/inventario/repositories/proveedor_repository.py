from inventario.models.proveedores import (
    Proveedor
)


class ProveedorRepository:

    @staticmethod
    def listar():

        return Proveedor.objects.all()

    @staticmethod
    def obtener(
        proveedor_id
    ):

        return Proveedor.objects.get(
            id=proveedor_id
        )

    @staticmethod
    def crear(
        **datos
    ):

        return Proveedor.objects.create(
            **datos
        )

    @staticmethod
    def actualizar(
        proveedor,
        datos
    ):

        for campo, valor in datos.items():

            setattr(
                proveedor,
                campo,
                valor
            )

        proveedor.save()

        return proveedor

    @staticmethod
    def eliminar(
        proveedor
    ):

        proveedor.delete()

    @staticmethod
    def existe_ruc(
        ruc
    ):

        return Proveedor.objects.filter(
            ruc=ruc
        ).exists()