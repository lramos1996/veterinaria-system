from datetime import date

from veterinaria.repositories.cita_repository import (
    CitaRepository
)

from shared.exceptions.business_exception import (
    BusinessException
)

from shared.validators.cita_validator import (
    CitaValidator
)

class CitaService:

    @staticmethod
    def listar():
        return CitaRepository.listar()

    @staticmethod
    def obtener(cita_id):

        try:
            return CitaRepository.obtener(
                cita_id
            )

        except Exception:
            raise BusinessException(
                "Cita no encontrada"
            )

    @staticmethod
    def crear(datos):

        if datos["fecha"] < date.today():

            raise BusinessException(
                "No se puede registrar una cita en una fecha pasada"
            )

        CitaValidator.validar_disponibilidad(
            datos["veterinario"],
            datos["fecha"],
            datos["hora"]
        )

        return CitaRepository.crear(
            **datos
        )

    @staticmethod
    def actualizar(cita_id, datos):

        cita = CitaService.obtener(
            cita_id
        )

        return CitaRepository.actualizar(
            cita,
            datos
        )

    @staticmethod
    def eliminar(cita_id):

        cita = CitaService.obtener(
            cita_id
        )

        CitaRepository.eliminar(
            cita
        )

    @staticmethod
    def buscar(
        fecha=None,
        veterinario=None,
        mascota=None
    ):

        return CitaRepository.buscar(
            fecha,
            veterinario,
            mascota
        )