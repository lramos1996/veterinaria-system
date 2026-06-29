from facturacion.models.ordenes_servicio import (
    OrdenServicio
)


class OrdenServicioRepository:

    @staticmethod
    def listar():

        return (
            OrdenServicio.objects.select_related(
                "cliente",
                "mascota"
            ).all()
        )

    @staticmethod
    def obtener(
        orden_id
    ):

        return (
            OrdenServicio.objects.select_related(
                "cliente",
                "mascota"
            ).get(
                id=orden_id
            )
        )

    @staticmethod
    def crear(
        **datos
    ):

        return OrdenServicio.objects.create(
            **datos
        )

    @staticmethod
    def actualizar(
        orden,
        datos
    ):

        for campo, valor in datos.items():

            setattr(
                orden,
                campo,
                valor
            )

        orden.save()

        return orden

    @staticmethod
    def eliminar(
        orden
    ):

        orden.delete()