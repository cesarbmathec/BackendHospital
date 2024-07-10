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

from .serializers import PacienteSerializer


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
