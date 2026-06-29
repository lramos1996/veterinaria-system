from rest_framework.routers import (
    DefaultRouter
)

from facturacion.views.orden_servicio_view import (
    OrdenServicioViewSet
)

router = DefaultRouter()

router.register(
    "",
    OrdenServicioViewSet,
    basename="ordenes-servicio"
)

urlpatterns = router.urls