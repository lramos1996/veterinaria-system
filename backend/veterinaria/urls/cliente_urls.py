from rest_framework.routers import (
    DefaultRouter
)

from veterinaria.views.cliente_view import (
    ClienteViewSet
)

router = DefaultRouter()

router.register(
    "",
    ClienteViewSet,
    basename='clientes'
)

urlpatterns = router.urls