from rest_framework.routers import DefaultRouter

from veterinaria.views.mascota_view import (
    MascotaViewSet
)

router = DefaultRouter()

router.register(
    "",
    MascotaViewSet,
    basename="mascotas"
)

urlpatterns = router.urls