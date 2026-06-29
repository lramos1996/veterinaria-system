from decimal import Decimal

from django.db import transaction

from inventario.models.proveedores import (
    Proveedor
)

from inventario.models.productos import (
    Producto
)

from inventario.repositories.compra_repository import (
    CompraRepository
)

from inventario.repositories.detalle_compra_repository import (
    DetalleCompraRepository
)

from inventario.services.movimientos_service import (
    MovimientoInventarioService
)

from inventario.repositories.detalle_compra_repository import (
    DetalleCompraRepository
)

class CompraService:

    @staticmethod
    def listar():

        return (
            CompraRepository.listar()
        )

    @staticmethod
    def obtener(
        compra_id
    ):

        return (
            CompraRepository.obtener(
                compra_id
            )
        )

    @staticmethod
    @transaction.atomic
    def crear(
        datos
    ):

        proveedor = (
            Proveedor.objects.get(
                id=datos["proveedor"]
            )
        )

        compra = (
            CompraRepository.crear(
                proveedor=proveedor,
                numero_documento=datos[
                    "numero_documento"
                ],
                observacion=datos.get(
                    "observacion",
                    ""
                ),
                total=0
            )
        )

        total = Decimal("0")

        for detalle in datos["detalles"]:

            producto = (
                Producto.objects.get(
                    id=detalle["producto"]
                )
            )

            subtotal = (
                detalle["cantidad"]
                *
                detalle["costo_unitario"]
            )

            DetalleCompraRepository.crear(
                compra=compra,
                producto=producto,
                cantidad=detalle[
                    "cantidad"
                ],
                costo_unitario=detalle[
                    "costo_unitario"
                ],
                subtotal=subtotal
            )

            MovimientoInventarioService.crear(
                {
                    "producto": producto,
                    "tipo": "ENTRADA",
                    "cantidad": detalle[
                        "cantidad"
                    ],
                    "observacion":
                        f"Compra {compra.id}"
                }
            )

            total += subtotal

        compra.total = total

        compra.save()

        return compra
    
    @staticmethod
    def listar_por_proveedor(
        proveedor_id
    ):

        return (
            CompraRepository
            .listar_por_proveedor(
                proveedor_id
            )
        )
    
    @staticmethod
    def listar_por_producto(
        producto_id
    ):

        return (
            DetalleCompraRepository
            .listar_por_producto(
                producto_id
            )
        )