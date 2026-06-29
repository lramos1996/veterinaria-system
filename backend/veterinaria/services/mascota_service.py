from veterinaria.repositories.cliente_repository import (
    ClienteRepository
)

from veterinaria.repositories.mascota_repository import (
    MascotaRepository
)

from shared.exceptions.business_exception import (
    BusinessException
)

from datetime import date

class MascotaService:

    @staticmethod
    def listar():

        return MascotaRepository.listar()

    @staticmethod
    def obtener(mascota_id):

        try:

            return MascotaRepository.obtener(
                mascota_id
            )

        except Exception:

            raise BusinessException(
                "Mascota no encontrada"
            )

    @staticmethod
    def obtener_propietario(cliente_id):

        try:

            return ClienteRepository.obtener(
                cliente_id
            )

        except Exception:

            raise BusinessException(
                "Cliente no encontrado"
            )

    @staticmethod
    def crear(datos):

        fecha_nacimiento = datos.get(
            "fecha_nacimiento"
        )

        if (
            fecha_nacimiento and
            fecha_nacimiento > date.today()
        ):

            raise BusinessException(
                "La fecha de nacimiento no puede ser futura"
            )

        propietario = (
            MascotaService.obtener_propietario(
                datos["propietario"]
            )
        )

        peso = datos.get("peso")

        if (
            peso is not None and
            float(peso) <= 0
        ):

            raise BusinessException(
                "El peso debe ser mayor a cero"
            )

        return MascotaRepository.crear(
            propietario=propietario,
            nombre=datos["nombre"],
            especie=datos["especie"],
            raza=datos["raza"],
            sexo=datos["sexo"],
            fecha_nacimiento=datos.get(
                "fecha_nacimiento"
            ),
            peso=datos.get(
                "peso"
            ),
            color=datos.get(
                "color",
                ""
            ),
            observaciones=datos.get(
                "observaciones",
                ""
            )
        )

    @staticmethod
    def actualizar(mascota_id, datos):

        mascota = MascotaService.obtener(
            mascota_id
        )

        if "propietario" in datos:

            datos["propietario"] = (
                MascotaService.obtener_propietario(
                    datos["propietario"]
                )
            )

        fecha_nacimiento = datos.get(
            "fecha_nacimiento"
        )

        if (
            fecha_nacimiento and
            fecha_nacimiento > date.today()
        ):

            raise BusinessException(
                "La fecha de nacimiento no puede ser futura"
            )

        propietario = (
            MascotaService.obtener_propietario(
                datos["propietario"]
            )
        )

        peso = datos.get("peso")

        if (
            peso is not None and
            float(peso) <= 0
        ):

            raise BusinessException(
                "El peso debe ser mayor a cero"
            )


        return MascotaRepository.actualizar(
            mascota,
            datos
        )

    @staticmethod
    def eliminar(mascota_id):

        mascota = MascotaService.obtener(
            mascota_id
        )

        MascotaRepository.eliminar(
            mascota
        )
        
    @staticmethod
    def buscar(
        nombre=None,
        especie=None,
        propietario=None
    ):

        return MascotaRepository.buscar(
            nombre,
            especie,
            propietario
        )