from veterinaria.repositories.cliente_repository import (
    ClienteRepository
)

from shared.exceptions.business_exception import (
    BusinessException
)


class ClienteService:

    @staticmethod
    def listar():
        return ClienteRepository.listar()

    @staticmethod
    def obtener(cliente_id):

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
        if not datos.get("documento"):
            raise BusinessException(
                "El documento es obligatorio"
            )
        
        if ClienteRepository.existe_documento(
                datos["documento"]
            ):

                raise BusinessException(
                    "El documento ya se encuentra registrado"
                )
        
        return ClienteRepository.crear(
            **datos
        )

    @staticmethod
    def actualizar(cliente_id, datos):

        cliente = ClienteService.obtener(
            cliente_id
        )

        if "documento" in datos:

            existe = (
                ClienteRepository
                .existe_documento(
                    datos["documento"]
                )
            )

            if (
                existe and
                cliente.documento != datos["documento"]
            ):

                raise BusinessException(
                    "El documento ya se encuentra registrado"
                )

        return ClienteRepository.actualizar(
            cliente,
            datos
        )

    @staticmethod
    def eliminar(cliente_id):

        cliente = ClienteService.obtener(
            cliente_id
        )

        ClienteRepository.eliminar(
            cliente
        )
        
    @staticmethod
    def buscar(
        documento=None,
        nombre=None
    ):

        return ClienteRepository.buscar(
            documento,
            nombre
        )