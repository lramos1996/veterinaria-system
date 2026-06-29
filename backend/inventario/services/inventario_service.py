from django.db import transaction

from inventario.models import MovimientoInventario

from inventario.repositories.producto_repository import (
    ProductoRepository
)

from inventario.repositories.kardex_repository import (
    KardexRepository
)


class InventarioService:

    @staticmethod
    @transaction.atomic
    def registrar_movimiento(
        producto_id,
        tipo,
        cantidad,
        observacion=""
    ):

        producto = (
            ProductoRepository.obtener_por_id(
                producto_id
            )
        )

        stock_anterior = producto.stock_actual

        if tipo == "ENTRADA":

            nuevo_stock = (
                stock_anterior + cantidad
            )

        elif tipo == "SALIDA":

            nuevo_stock = (
                stock_anterior - cantidad
            )

        else:

            raise Exception(
                "Tipo de movimiento inválido"
            )

        producto.stock_actual = nuevo_stock

        ProductoRepository.guardar(
            producto
        )

        movimiento = (
            MovimientoInventario.objects.create(
                producto=producto,
                tipo=tipo,
                cantidad=cantidad,
                observacion=observacion
            )
        )

        KardexRepository.crear(
            producto=producto,
            tipo_movimiento=tipo,
            cantidad=cantidad,
            stock_anterior=stock_anterior,
            stock_nuevo=nuevo_stock,
            referencia=f"MOV-{movimiento.id}"
        )

        return movimiento