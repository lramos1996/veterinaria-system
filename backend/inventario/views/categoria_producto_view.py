# inventario/views/categoria_producto_view.py

from shared.views.crud_view import (
    CrudViewSet
)

from inventario.services.categoria_producto_service import (
    CategoriaProductoService
)

from inventario.serializers.categoria_producto_serializer import (
    CategoriaProductoSerializer
)


class CategoriaProductoViewSet(
    CrudViewSet
):

    service = (
        CategoriaProductoService
    )

    serializer_class = (
        CategoriaProductoSerializer
    )