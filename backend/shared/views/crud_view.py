from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class CrudViewSet(
    ViewSet
):

    service = None
    serializer_class = None

    def list(
        self,
        request
    ):

        objetos = self.service.listar()

        serializer = (
            self.serializer_class(
                objetos,
                many=True
            )
        )

        return Response(
            serializer.data
        )

    def retrieve(
        self,
        request,
        pk=None
    ):

        objeto = self.service.obtener(
            pk
        )

        serializer = (
            self.serializer_class(
                objeto
            )
        )

        return Response(
            serializer.data
        )

    def create(
        self,
        request
    ):

        serializer = (
            self.serializer_class(
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        objeto = self.service.crear(
            serializer.validated_data
        )

        serializer = (
            self.serializer_class(
                objeto
            )
        )

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    def update(
        self,
        request,
        pk=None
    ):

        objeto_actual = self.service.obtener(
            pk
        )

        serializer = (
            self.serializer_class(
                objeto_actual,
                data=request.data
            )
        )

        serializer.is_valid(
            raise_exception=True
        )

        objeto = self.service.actualizar(
            pk,
            serializer.validated_data
        )

        serializer = (
            self.serializer_class(
                objeto
            )
        )

        return Response(
            serializer.data
        )