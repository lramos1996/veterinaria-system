from django.db.models import (
    Sum,
    Count,
    F
)

from facturacion.models.comprobantes import (
    Comprobante
)

from facturacion.models.detalle_comprobantes import (
    DetalleComprobante
)


class ComprobanteRepository:

    @staticmethod
    def listar():

        return (
            Comprobante.objects.select_related(
                "tipo",
                "orden_servicio",
                "orden_servicio__cliente",
                "orden_servicio__mascota"
            )
            .all()
            .order_by("-fecha_emision")
        )

    @staticmethod
    def obtener(
        comprobante_id
    ):

        return (
            Comprobante.objects.select_related(
                "tipo",
                "orden_servicio",
                "orden_servicio__cliente",
                "orden_servicio__mascota"
            ).get(
                id=comprobante_id
            )
        )

    @staticmethod
    def crear(
        **datos
    ):

        return Comprobante.objects.create(
            **datos
        )

    @staticmethod
    def dashboard():

        comprobantes = Comprobante.objects.all()

        total_ventas = (
            comprobantes.aggregate(
                total=Sum("total")
            )["total"] or 0
        )

        total_igv = (
            comprobantes.aggregate(
                total=Sum("igv")
            )["total"] or 0
        )

        total_subtotal = (
            comprobantes.aggregate(
                total=Sum("subtotal")
            )["total"] or 0
        )

        cantidad = comprobantes.count()

        ticket_promedio = (
            total_ventas / cantidad
            if cantidad > 0 else 0
        )

        return {
            "cantidad_comprobantes": cantidad,
            "subtotal_total": total_subtotal,
            "igv_total": total_igv,
            "ventas_total": total_ventas,
            "ticket_promedio": ticket_promedio
        }

    @staticmethod
    def listar_por_fecha(
        desde,
        hasta
    ):

        return (
            Comprobante.objects.select_related(
                "tipo",
                "orden_servicio",
                "orden_servicio__cliente",
                "orden_servicio__mascota"
            )
            .filter(
                fecha_emision__date__gte=desde,
                fecha_emision__date__lte=hasta
            )
            .order_by("-fecha_emision")
        )

    @staticmethod
    def recientes(
        limite=10
    ):

        return (
            Comprobante.objects.select_related(
                "tipo",
                "orden_servicio",
                "orden_servicio__cliente",
                "orden_servicio__mascota"
            )
            .all()
            .order_by("-fecha_emision")[:limite]
        )

    @staticmethod
    def productos_mas_vendidos():

        return (
            DetalleComprobante.objects.filter(
                producto__isnull=False
            )
            .values(
                "producto",
                "producto__nombre",
                "producto__codigo"
            )
            .annotate(
                total_cantidad=Sum("cantidad"),
                total_ventas=Sum("subtotal")
            )
            .order_by("-total_cantidad")
        )

    @staticmethod
    def clientes_top():

        return (
            Comprobante.objects.values(
                "orden_servicio__cliente",
                "orden_servicio__cliente__nombres",
                "orden_servicio__cliente__apellidos"
            )
            .annotate(
                cantidad_comprobantes=Count("id"),
                total_comprado=Sum("total")
            )
            .order_by("-total_comprado")
        )