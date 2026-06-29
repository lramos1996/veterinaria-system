from rest_framework.routers import (
    DefaultRouter
)

from veterinaria.views.veterinario_view import (
    VeterinarioViewSet
)

router = DefaultRouter()

router.register(
    "",
    VeterinarioViewSet,
    basename="veterinario"
)

urlpatterns = router.urls