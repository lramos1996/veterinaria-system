from rest_framework.routers import (
    DefaultRouter
)

from inventario.views.movimientos_view import (
    MovimientoInventarioViewSet
)

router = DefaultRouter()

router.register(
    "",
    MovimientoInventarioViewSet,
    basename="movimiento-inventario"
)

urlpatterns = router.urls