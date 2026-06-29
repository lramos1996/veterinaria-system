from facturacion.models.detalle_comprobantes import (
    DetalleComprobante
)


class DetalleComprobanteRepository:

    @staticmethod
    def listar():

        return (
            DetalleComprobante.objects.select_related(
                "comprobante",
                "producto"
            ).all()
        )

    @staticmethod
    def obtener(
        detalle_id
    ):

        return (
            DetalleComprobante.objects.select_related(
                "comprobante",
                "producto"
            ).get(
                id=detalle_id
            )
        )

    @staticmethod
    def crear(
        **datos
    ):

        return DetalleComprobante.objects.create(
            **datos
        )

    @staticmethod
    def listar_por_comprobante(
        comprobante_id
    ):

        return (
            DetalleComprobante.objects.select_related(
                "producto"
            ).filter(
                comprobante_id=comprobante_id
            ).order_by("id")
        )