from rest_framework.routers import DefaultRouter

from veterinaria.views.historia_clinica_view import (
    HistoriaClinicaViewSet
)

router = DefaultRouter()

router.register(
    "",
    HistoriaClinicaViewSet,
    basename="historias-clinicas"
)

urlpatterns = router.urls