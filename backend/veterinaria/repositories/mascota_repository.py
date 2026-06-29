from veterinaria.models.mascotas import Mascota


class MascotaRepository:

    @staticmethod
    def listar():
        return Mascota.objects.select_related(
            "propietario"
        ).all()

    @staticmethod
    def obtener(mascota_id):
        return Mascota.objects.get(
            id=mascota_id
        )

    @staticmethod
    def crear(**datos):
        return Mascota.objects.create(
            **datos
        )

    @staticmethod
    def actualizar(mascota, datos):

        for campo, valor in datos.items():
            setattr(
                mascota,
                campo,
                valor
            )

        mascota.save()

        return mascota

    @staticmethod
    def eliminar(mascota):
        mascota.delete()

    @staticmethod
    def buscar(
        nombre=None,
        especie=None,
        propietario=None
    ):

        queryset = Mascota.objects.select_related(
            "propietario"
        )

        if nombre:

            queryset = queryset.filter(
                nombre__icontains=nombre
            )

        if especie:

            queryset = queryset.filter(
                especie__icontains=especie
            )

        if propietario:

            queryset = queryset.filter(
                propietario_id=propietario
            )

        return queryset