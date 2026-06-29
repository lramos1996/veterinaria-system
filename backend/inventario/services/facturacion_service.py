from facturacion.models import (
    OrdenServicio,
    Comprobante
)


class FacturacionService:

    @staticmethod
    def generar_orden_servicio(
        cliente,
        mascota
    ):

        ultima = (
            OrdenServicio.objects
            .order_by("-id")
            .first()
        )

        correlativo = (
            ultima.id + 1
            if ultima
            else 1
        )

        return OrdenServicio.objects.create(
            numero=f"OS{correlativo:06d}",
            cliente=cliente,
            mascota=mascota
        )