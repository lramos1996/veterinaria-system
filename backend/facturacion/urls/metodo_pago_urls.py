from rest_framework.routers import (
    DefaultRouter
)

from facturacion.views.metodo_pago_view import (
    MetodoPagoViewSet
)

router = DefaultRouter()

router.register(
    "",
    MetodoPagoViewSet,
    basename="metodos-pago"
)

urlpatterns = router.urls