from rest_framework.routers import (
    DefaultRouter
)

from inventario.views.compra_view import (
    CompraViewSet
)

router = DefaultRouter()

router.register(
    "",
    CompraViewSet,
    basename="compra"
)

urlpatterns = router.urls