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


class HistoriaClinicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoriaClinica
        fields = "__all__"


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = "__all_"


class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = "__all_"


class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = "__all_"


class PrescripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescripcion
        fields = "__all_"
