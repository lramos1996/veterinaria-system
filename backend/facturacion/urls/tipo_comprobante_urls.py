from rest_framework.routers import (
    DefaultRouter
)

from facturacion.views.tipo_comprobante_view import (
    TipoComprobanteViewSet
)

router = DefaultRouter()

router.register(
    "",
    TipoComprobanteViewSet,
    basename="tipos-comprobante"
)

urlpatterns = router.urls