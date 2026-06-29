from veterinaria.repositories.veterinario_repository import (
    VeterinarioRepository
)

from shared.exceptions.business_exception import (
    BusinessException
)


class VeterinarioService:

    @staticmethod
    def listar():

        return VeterinarioRepository.listar()

    @staticmethod
    def obtener(veterinario_id):

        try:

            return VeterinarioRepository.obtener(
                veterinario_id
            )

        except Exception:

            raise BusinessException(
                "Veterinario no encontrado"
            )

    @staticmethod
    def crear(datos):

        if VeterinarioRepository.existe_colegiatura(
            datos["colegiatura"]
        ):

            raise BusinessException(
                "La colegiatura ya se encuentra registrada"
            )

        return VeterinarioRepository.crear(
            **datos
        )

    @staticmethod
    def actualizar(
        veterinario_id,
        datos
    ):

        veterinario = (
            VeterinarioService.obtener(
                veterinario_id
            )
        )

        nueva_colegiatura = datos.get(
            "colegiatura"
        )

        if (
            nueva_colegiatura
            and
            nueva_colegiatura
            != veterinario.colegiatura
            and
            VeterinarioRepository.existe_colegiatura(
                nueva_colegiatura
            )
        ):

            raise BusinessException(
                "La colegiatura ya se encuentra registrada"
            )

        return VeterinarioRepository.actualizar(
            veterinario,
            datos
        )

    @staticmethod
    def eliminar(veterinario_id):

        veterinario = VeterinarioService.obtener(
            veterinario_id
        )

        VeterinarioRepository.eliminar(
            veterinario
        )

    @staticmethod
    def buscar(
        especialidad=None,
        activo=None
    ):

        return VeterinarioRepository.buscar(
            especialidad,
            activo
        )