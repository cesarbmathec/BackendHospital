from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("paciente/", views.PacienteList.as_view(), name="paciente-list"),
    path("paciente/<int:pk>/", views.PacienteDetail.as_view(), name="paciente-detail"),
]
