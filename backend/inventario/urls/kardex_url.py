from rest_framework.routers import (
    DefaultRouter
)

from inventario.views.kardex_view import (
    KardexViewSet
)

router = DefaultRouter()

router.register(
    "",
    KardexViewSet,
    basename="kardex"
)

urlpatterns = router.urls