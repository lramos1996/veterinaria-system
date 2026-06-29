# inventario/repositories/categoria_producto_repository.py

from inventario.models.categorias import (
    CategoriaProducto
)


class CategoriaProductoRepository:

    @staticmethod
    def listar():

        return CategoriaProducto.objects.all()

    @staticmethod
    def obtener(
        categoria_id
    ):

        return CategoriaProducto.objects.get(
            id=categoria_id
        )

    @staticmethod
    def crear(
        **datos
    ):

        return CategoriaProducto.objects.create(
            **datos
        )

    @staticmethod
    def actualizar(
        categoria,
        datos
    ):

        for campo, valor in datos.items():

            setattr(
                categoria,
                campo,
                valor
            )

        categoria.save()

        return categoria

    @staticmethod
    def eliminar(
        categoria
    ):

        categoria.delete()

    @staticmethod
    def existe_nombre(
        nombre
    ):

        return CategoriaProducto.objects.filter(
            nombre=nombre
        ).exists()