from veterinaria.models.clientes import Cliente


class ClienteRepository:

    @staticmethod
    def listar():
        return Cliente.objects.all()

    @staticmethod
    def obtener(cliente_id):
        return Cliente.objects.get(id=cliente_id)

    @staticmethod
    def crear(**datos):
        return Cliente.objects.create(**datos)

    @staticmethod
    def existe_documento(
        documento
    ):

        return Cliente.objects.filter(
            documento=documento
        ).exists()


    @staticmethod
    def actualizar(cliente, datos):

        for campo, valor in datos.items():
            setattr(cliente, campo, valor)

        cliente.save()

        return cliente

    @staticmethod
    def eliminar(cliente):
        cliente.delete()

    @staticmethod
    def buscar(
        documento=None,
        nombre=None
    ):

        queryset = Cliente.objects.all()

        if documento:

            queryset = queryset.filter(
                documento=documento
            )

        if nombre:

            queryset = queryset.filter(
                nombres__icontains=nombre
            )

        return queryset