from decimal import Decimal

from facturacion.models.ordenes_servicio import (
    OrdenServicio
)

from inventario.models.productos import (
    Producto
)

from facturacion.repositories.detalle_orden_servicio_repository import (
    DetalleOrdenServicioRepository
)

from facturacion.services.orden_servicio_service import (
    OrdenServicioService
)

from shared.exceptions.business_exception import (
    BusinessException
)


class DetalleOrdenServicioService:

    @staticmethod
    def listar():

        return (
            DetalleOrdenServicioRepository.listar()
        )

    @staticmethod
    def obtener(
        detalle_id
    ):

        try:

            return (
                DetalleOrdenServicioRepository.obtener(
                    detalle_id
                )
            )

        except Exception:

            raise BusinessException(
                "Detalle de orden no encontrado"
            )

    @staticmethod
    def crear(
        datos
    ):

        orden = datos["orden_servicio"]

        if orden.estado == "FACTURADA":

            raise BusinessException(
                "No se puede agregar detalles a una orden facturada"
            )

        producto = datos.get("producto")
        cantidad = datos["cantidad"]
        precio_unitario = datos["precio_unitario"]

        if cantidad <= 0:

            raise BusinessException(
                "La cantidad debe ser mayor a 0"
            )

        if precio_unitario < 0:

            raise BusinessException(
                "El precio unitario no puede ser negativo"
            )

        if producto:

            producto = Producto.objects.get(
                id=producto.id
            )

            if not datos.get("descripcion"):

                datos["descripcion"] = (
                    producto.nombre
                )

        datos["subtotal"] = (
            Decimal(cantidad)
            * Decimal(precio_unitario)
        )

        detalle = (
            DetalleOrdenServicioRepository.crear(
                **datos
            )
        )

        OrdenServicioService.recalcular_total(
            orden.id
        )

        return detalle

    @staticmethod
    def actualizar(
        detalle_id,
        datos
    ):

        detalle = (
            DetalleOrdenServicioService.obtener(
                detalle_id
            )
        )

        orden = detalle.orden_servicio

        if orden.estado == "FACTURADA":

            raise BusinessException(
                "No se puede modificar detalles de una orden facturada"
            )

        producto = datos.get(
            "producto",
            detalle.producto
        )

        cantidad = datos.get(
            "cantidad",
            detalle.cantidad
        )

        precio_unitario = datos.get(
            "precio_unitario",
            detalle.precio_unitario
        )

        descripcion = datos.get(
            "descripcion",
            detalle.descripcion
        )

        if cantidad <= 0:

            raise BusinessException(
                "La cantidad debe ser mayor a 0"
            )

        if precio_unitario < 0:

            raise BusinessException(
                "El precio unitario no puede ser negativo"
            )

        if producto and not descripcion:

            descripcion = producto.nombre

        datos["descripcion"] = descripcion
        datos["subtotal"] = (
            Decimal(cantidad)
            * Decimal(precio_unitario)
        )

        detalle = (
            DetalleOrdenServicioRepository.actualizar(
                detalle,
                datos
            )
        )

        OrdenServicioService.recalcular_total(
            orden.id
        )

        return detalle

    @staticmethod
    def eliminar(
        detalle_id
    ):

        detalle = (
            DetalleOrdenServicioService.obtener(
                detalle_id
            )
        )

        orden = detalle.orden_servicio

        if orden.estado == "FACTURADA":

            raise BusinessException(
                "No se puede eliminar detalles de una orden facturada"
            )

        DetalleOrdenServicioRepository.eliminar(
            detalle
        )

        OrdenServicioService.recalcular_total(
            orden.id
        )