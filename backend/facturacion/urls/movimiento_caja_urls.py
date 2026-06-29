from rest_framework.routers import (
    DefaultRouter
)

from facturacion.views.movimiento_caja_view import (
    MovimientoCajaViewSet
)

router = DefaultRouter()

router.register(
    "",
    MovimientoCajaViewSet,
    basename="movimientos-caja"
)

urlpatterns = router.urls