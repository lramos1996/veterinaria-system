from rest_framework.routers import (
    DefaultRouter
)

from facturacion.views.detalle_orden_servicio_view import (
    DetalleOrdenServicioViewSet
)

router = DefaultRouter()

router.register(
    "",
    DetalleOrdenServicioViewSet,
    basename="detalles-orden-servicio"
)

urlpatterns = router.urls