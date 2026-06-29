from inventario.models.productos import (
    Producto
)
from django.db import models

class ProductoRepository:

    @staticmethod
    def listar():

        return Producto.objects.select_related(
            "categoria"
        ).all()

    @staticmethod
    def obtener(
        producto_id
    ):

        return Producto.objects.get(
            id=producto_id
        )

    @staticmethod
    def crear(
        **datos
    ):

        return Producto.objects.create(
            **datos
        )

    @staticmethod
    def actualizar(
        producto,
        datos
    ):

        for campo, valor in datos.items():

            setattr(
                producto,
                campo,
                valor
            )

        producto.save()

        return producto

    @staticmethod
    def eliminar(
        producto
    ):

        producto.delete()

    @staticmethod
    def existe_codigo(
        codigo
    ):

        return Producto.objects.filter(
            codigo=codigo
        ).exists()
    
    @staticmethod
    def stock_bajo():

       return (
            Producto.objects.filter(
                stock_actual__lte=models.F(
                    "stock_minimo"
                ),
                activo=True
            )
            .order_by(
                "stock_actual"
            )
        )
    
    @staticmethod
    def dashboard():

        productos = (
            Producto.objects.filter(
                activo=True
            )
        )

        valor_inventario = sum(
            producto.stock_actual
            * producto.costo
            for producto in productos
        )

        return {
            "total_productos":
                Producto.objects.count(),

            "productos_activos":
                productos.count(),

            "productos_stock_bajo":
                productos.filter(
                    stock_actual__lte=models.F(
                        "stock_minimo"
                    )
                ).count(),

            "valor_inventario":
                valor_inventario
        }
    
    @staticmethod
    def reposicion():

        return (
            Producto.objects.filter(
                stock_actual__lte=models.F(
                    "stock_minimo"
                ),
                activo=True
            )
            .order_by(
                "stock_actual"
            )
        )