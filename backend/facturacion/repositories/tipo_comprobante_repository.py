from facturacion.models.tipos_comprobante import (
    TipoComprobante
)


class TipoComprobanteRepository:

    @staticmethod
    def listar():

        return TipoComprobante.objects.all()

    @staticmethod
    def obtener(
        tipo_id
    ):

        return TipoComprobante.objects.get(
            id=tipo_id
        )

    @staticmethod
    def crear(
        **datos
    ):

        return TipoComprobante.objects.create(
            **datos
        )

    @staticmethod
    def actualizar(
        tipo,
        datos
    ):

        for campo, valor in datos.items():

            setattr(
                tipo,
                campo,
                valor
            )

        tipo.save()

        return tipo

    @staticmethod
    def eliminar(
        tipo
    ):

        tipo.delete()