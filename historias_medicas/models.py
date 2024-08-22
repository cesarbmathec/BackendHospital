from django.db import models


class Paciente(models.Model):
    GENERO_CHOICES = [
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("O", "Otro"),
    ]

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo_electronico = models.EmailField(blank=True, null=True)
    cedula_identidad = models.CharField(
        max_length=20, unique=True
    )  # Ahora obligatorio y único

    def __str__(self):
        return "{0} {1}".format(self.nombre, self.apellido)


class Medico(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    correo_electronico = models.EmailField(blank=True, null=True)

    def __str__(self):
        return "Dr. {0} {1} ({2})".format(self.nombre, self.apellido, self.especialidad)


class HistoriaClinica(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha_creacion = models.DateField(auto_now_add=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Historia Clinica de {0} {1}".format(
            self.paciente.nombre, self.paciente.apellido
        )


class Hospitalizacion(models.Model):
    historia_clinica = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)
    fecha_ingreso = models.DateField()
    fecha_salida = models.DateField(blank=True, null=True)

    def __str__(self):
        return "Hospitalización desde {0}".format(self.fecha_ingreso)


class Consulta(models.Model):
    historia_clinica = models.ForeignKey(HistoriaClinica, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha_consulta = models.DateField()
    diagnostico = models.TextField(blank=True, null=True)
    tratamiento = models.TextField(blank=True, null=True)
    notas = models.TextField(blank=True, null=True)

    def __str__(self):
        return "Consulta el {0} por {1} {2}".format(
            self.fecha_consulta, self.medico.nombre, self.medico.apellido
        )


class Medicamento(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    dosis = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Prescripcion(models.Model):
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    dosis = models.CharField(max_length=50)
    duracion = models.CharField(max_length=50)

    def __str__(self):
        return "{0} prescrito en {1}".format(
            self.medicamento.nombre, self.consulta.fecha_consulta
        )
