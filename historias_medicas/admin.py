from django.contrib import admin

from .models import (
    Paciente,
    Medico,
    HistoriaClinica,
    Consulta,
    Medicamento,
    Prescripcion,
)

admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(HistoriaClinica)
admin.site.register(Consulta)
admin.site.register(Medicamento)
admin.site.register(Prescripcion)
