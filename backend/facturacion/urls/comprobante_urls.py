from rest_framework.routers import (
    DefaultRouter
)

from facturacion.views.comprobante_view import (
    ComprobanteViewSet
)

router = DefaultRouter()

router.register(
    "",
    ComprobanteViewSet,
    basename="comprobantes"
)

urlpatterns = router.urls