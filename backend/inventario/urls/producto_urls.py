from rest_framework.routers import (
    DefaultRouter
)

from inventario.views.producto_view import (
    ProductoViewSet
)

router = DefaultRouter()

router.register(
    "",
    ProductoViewSet,
    basename="producto"
)

urlpatterns = router.urls