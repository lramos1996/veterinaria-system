from veterinaria.models.veterinarios import (
    Veterinario
)


class VeterinarioRepository:

    @staticmethod
    def listar():

        return Veterinario.objects.all()

    @staticmethod
    def obtener(veterinario_id):

        return Veterinario.objects.get(
            id=veterinario_id
        )

    @staticmethod
    def existe_colegiatura(
        colegiatura
    ):

        return Veterinario.objects.filter(
            colegiatura=colegiatura
        ).exists()

    @staticmethod
    def crear(**datos):

        return Veterinario.objects.create(
            **datos
        )

    @staticmethod
    def actualizar(
        veterinario,
        datos
    ):

        for campo, valor in datos.items():

            setattr(
                veterinario,
                campo,
                valor
            )

        veterinario.save()

        return veterinario

    @staticmethod
    def eliminar(veterinario):
        veterinario.delete()

    @staticmethod
    def buscar(
        especialidad=None,
        activo=None
    ):

        queryset = Veterinario.objects.all()

        if especialidad:

            queryset = queryset.filter(
                especialidad__icontains=especialidad
            )

        if activo is not None:

            queryset = queryset.filter(
                activo=activo
            )

        return queryset