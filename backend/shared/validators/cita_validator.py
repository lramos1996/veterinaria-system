from shared.exceptions.business_exception import (
    BusinessException
)

from veterinaria.repositories.cita_repository import (
    CitaRepository
)


class CitaValidator:

    @staticmethod
    def validar_disponibilidad(
        veterinario_id,
        fecha,
        hora
    ):

        existe = (
            CitaRepository.existe_conflicto(
                veterinario_id,
                fecha,
                hora
            )
        )

        if existe:

            raise BusinessException(
                "El veterinario ya tiene una cita programada en ese horario"
            )