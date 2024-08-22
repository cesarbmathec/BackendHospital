from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("paciente/", views.PacienteList.as_view(), name="paciente-list"),
    path("paciente/<int:pk>/", views.PacienteDetail.as_view(), name="paciente-detail"),
    path("medico/", views.MedicoList.as_view(), name="medico-list"),
    path("medico/<int:pk>/", views.MedicoDetail.as_view(), name="medico-detail"),
    path(
        "historia_clinica/",
        views.HistoriaClinicaList.as_view(),
        name="historia-clinica-list",
    ),
    path(
        "historia_clinica/<int:pk>/",
        views.HistoriaClinicaDetail.as_view(),
        name="historia-clinica-detail",
    ),
    path("consulta/", views.ConsultaList.as_view(), name="consulta-list"),
    path("consulta/<int:pk>/", views.ConsultaDetail.as_view(), name="consulta-detail"),
    path("medicamento/", views.MedicamentoList.as_view(), name="medicamento-list"),
    path(
        "medicamento/<int:pk>/",
        views.MedicamentoDetail.as_view(),
        name="medicamento-detail",
    ),
    path("prescripcion/", views.PrescripcionList.as_view(), name="prescripcion-list"),
    path(
        "prescripcion/<int:pk>/",
        views.PrescripcionDetail.as_view(),
        name="prescripcion-detail",
    ),
]
