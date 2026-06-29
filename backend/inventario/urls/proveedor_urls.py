from rest_framework.routers import (
    DefaultRouter
)

from inventario.views.proveedor_view import (
    ProveedorViewSet
)

router = DefaultRouter()

router.register(
    "",
    ProveedorViewSet,
    basename="proveedor"
)

urlpatterns = router.urls