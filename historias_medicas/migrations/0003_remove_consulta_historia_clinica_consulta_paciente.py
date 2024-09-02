# Generated by Django 5.0.6 on 2024-08-30 02:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historias_medicas', '0002_hospitalizacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='historia_clinica',
        ),
        migrations.AddField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='historias_medicas.paciente'),
            preserve_default=False,
        ),
    ]
