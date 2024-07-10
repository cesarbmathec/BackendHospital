from rest_framework import serializers

from .models import (
    Paciente,
    Medico,
    HistoriaClinica,
    Consulta,
    Medicamento,
    Prescripcion,
)


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = "__all__"
