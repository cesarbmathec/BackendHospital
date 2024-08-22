from django.http import HttpResponse
from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .models import (
    Paciente,
    Medico,
    HistoriaClinica,
    Consulta,
    Medicamento,
    Prescripcion,
)

from .serializers import (
    PacienteSerializer,
    HistoriaClinicaSerializer,
    ConsultaSerializer,
    MedicoSerializer,
    MedicamentoSerializer,
    PrescripcionSerializer,
)


def index(request):
    return HttpResponse("Hello, world. You're at the Historias Médicas index.")


@permission_classes([IsAuthenticated])
class PacienteList(generics.ListCreateAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


@permission_classes([IsAuthenticated])
class PacienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


@permission_classes([IsAuthenticated])
class HistoriaClinicaList(generics.ListCreateAPIView):
    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaClinicaSerializer


@permission_classes([IsAuthenticated])
class HistoriaClinicaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistoriaClinica.objects.all()
    serializer_class = HistoriaClinicaSerializer


@permission_classes([IsAuthenticated])
class ConsultaList(generics.ListCreateAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer


@permission_classes([IsAuthenticated])
class ConsultaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer


@permission_classes([IsAuthenticated])
class MedicoList(generics.ListCreateAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer


@permission_classes([IsAuthenticated])
class MedicoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer


@permission_classes([IsAuthenticated])
class MedicamentoList(generics.ListCreateAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer


@permission_classes([IsAuthenticated])
class MedicamentoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer


@permission_classes([IsAuthenticated])
class PrescripcionList(generics.ListCreateAPIView):
    queryset = Prescripcion.objects.all()
    serializer_class = PrescripcionSerializer


@permission_classes([IsAuthenticated])
class PrescripcionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescripcion.objects.all()
    serializer_class = PrescripcionSerializer
