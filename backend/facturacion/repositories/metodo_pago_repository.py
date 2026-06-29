from facturacion.models.pagos import (
    MetodoPago
)


class MetodoPagoRepository:

    @staticmethod
    def listar():

        return MetodoPago.objects.all()

    @staticmethod
    def obtener(
        metodo_pago_id
    ):

        return MetodoPago.objects.get(
            id=metodo_pago_id
        )

    @staticmethod
    def crear(
        **datos
    ):

        return MetodoPago.objects.create(
            **datos
        )

    @staticmethod
    def actualizar(
        metodo_pago,
        datos
    ):

        for campo, valor in datos.items():

            setattr(
                metodo_pago,
                campo,
                valor
            )

        metodo_pago.save()

        return metodo_pago

    @staticmethod
    def eliminar(
        metodo_pago
    ):

        metodo_pago.delete()