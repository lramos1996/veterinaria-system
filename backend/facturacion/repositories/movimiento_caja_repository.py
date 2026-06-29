from django.db.models import Sum

from facturacion.models.caja import (
    MovimientoCaja
)


class MovimientoCajaRepository:

    @staticmethod
    def listar():

        return (
            MovimientoCaja.objects.select_related(
                "comprobante",
                "metodo_pago"
            ).all().order_by("-fecha")
        )

    @staticmethod
    def obtener(
        movimiento_id
    ):

        return (
            MovimientoCaja.objects.select_related(
                "comprobante",
                "metodo_pago"
            ).get(
                id=movimiento_id
            )
        )

    @staticmethod
    def crear(
        **datos
    ):

        return MovimientoCaja.objects.create(
            **datos
        )

    @staticmethod
    def ingresos_total():

        return (
            MovimientoCaja.objects.filter(
                tipo="INGRESO"
            ).aggregate(
                total=Sum("monto")
            )["total"] or 0
        )

    @staticmethod
    def egresos_total():

        return (
            MovimientoCaja.objects.filter(
                tipo="EGRESO"
            ).aggregate(
                total=Sum("monto")
            )["total"] or 0
        )

    @staticmethod
    def ultimos_movimientos(
        limite=10
    ):

        return (
            MovimientoCaja.objects.select_related(
                "comprobante",
                "metodo_pago"
            )
            .all()
            .order_by("-fecha")[:limite]
        )