from rest_framework.routers import DefaultRouter

from veterinaria.views.cita_view import (
    CitaViewSet
)

router = DefaultRouter()

router.register(
    "",
    CitaViewSet,
    basename="citas"
)

urlpatterns = router.urls