# inventario/urls/categoria_producto_urls.py

from rest_framework.routers import (
    DefaultRouter
)

from inventario.views.categoria_producto_view import (
    CategoriaProductoViewSet
)

router = DefaultRouter()

router.register(
    "",
    CategoriaProductoViewSet,
    basename="categoria-producto"
)

urlpatterns = router.urls