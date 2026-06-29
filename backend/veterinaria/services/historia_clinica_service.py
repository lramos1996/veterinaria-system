from veterinaria.models import (
    Mascota,
    Veterinario
)

from veterinaria.repositories.historia_clinica_repository import (
    HistoriaClinicaRepository
)

from shared.exceptions.business_exception import (
    BusinessException
)

class HistoriaClinicaService:

    @staticmethod
    def listar():

        return HistoriaClinicaRepository.listar()

    @staticmethod
    def obtener(id):
        try:

            return HistoriaClinicaRepository.obtener(
                id
            )

        except Exception:

            raise BusinessException(
                "Historia clínica no encontrada"
            )


    @staticmethod
    def crear(datos):

        mascota = Mascota.objects.get(
            pk=datos["mascota"]
        )

        veterinario = Veterinario.objects.get(
            pk=datos["veterinario"]
        )

        return HistoriaClinicaRepository.crear(
            mascota=mascota,
            veterinario=veterinario,
            fecha_atencion=datos["fecha_atencion"],
            peso=datos.get("peso"),
            temperatura=datos.get("temperatura"),
            anamnesis=datos["anamnesis"],
            diagnostico=datos["diagnostico"],
            tratamiento=datos["tratamiento"],
            observaciones=datos.get(
                "observaciones",
                ""
            )
        )
    
    @staticmethod
    def actualizar(historial_id, datos):

        historial = HistoriaClinicaService.obtener(
            historial_id
        )

        return HistoriaClinicaRepository.actualizar(
            historial,
            datos
        )

    @staticmethod
    def eliminar(historial_id):

        historial = HistoriaClinicaService.obtener(
            historial_id
        )

        HistoriaClinicaRepository.eliminar(
            historial
        )

    @staticmethod
    def buscar(
        mascota=None,
        veterinario=None
    ):

        return HistoriaClinicaRepository.buscar(
            mascota,
            veterinario
        )