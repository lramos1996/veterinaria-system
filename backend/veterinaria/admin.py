from django.contrib import admin

from .models import Cliente
from .models import Mascota
from .models import Veterinario
from .models import Cita
from .models import HistoriaClinica


admin.site.register(Cliente)
admin.site.register(Mascota)
admin.site.register(Veterinario)
admin.site.register(Cita)
admin.site.register(HistoriaClinica)