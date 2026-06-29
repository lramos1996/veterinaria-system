from facturacion.models.detalle_ordenes_servicio import (
    DetalleOrdenServicio
)


class DetalleOrdenServicioRepository:

    @staticmethod
    def listar():

        return (
            DetalleOrdenServicio.objects
            .select_related(
                "orden_servicio",
                "producto"
            )
            .all()
        )

    @staticmethod
    def obtener(
        detalle_id
    ):

        return (
            DetalleOrdenServicio.objects
            .select_related(
                "orden_servicio",
                "producto"
            )
            .get(
                id=detalle_id
            )
        )

    @staticmethod
    def crear(
        **datos
    ):

        return DetalleOrdenServicio.objects.create(
            **datos
        )

    @staticmethod
    def actualizar(
        detalle,
        datos
    ):

        for campo, valor in datos.items():

            setattr(
                detalle,
                campo,
                valor
            )

        detalle.save()

        return detalle

    @staticmethod
    def eliminar(
        detalle
    ):

        detalle.delete()

    @staticmethod
    def listar_por_orden(
        orden_id
    ):

        return (
            DetalleOrdenServicio.objects
            .select_related(
                "producto"
            )
            .filter(
                orden_servicio_id=orden_id
            )
            .order_by("id")
        )