# Generated by Django 5.1.5 on 2025-02-08 23:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encargado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('especialidad', models.CharField(blank=True, max_length=100, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='encargados/')),
            ],
        ),
        migrations.CreateModel(
            name='Estructura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=255)),
                ('fecha_construccion', models.DateField()),
                ('estado', models.CharField(choices=[('Bueno', 'Bueno'), ('Regular', 'Regular'), ('Malo', 'Malo')], max_length=50)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='estructuras/')),
            ],
        ),
        migrations.CreateModel(
            name='PlanMantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Preventivo', 'Preventivo'), ('Correctivo', 'Correctivo')], max_length=50)),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso'), ('Finalizado', 'Finalizado')], max_length=50)),
                ('documento', models.FileField(blank=True, null=True, upload_to='planes_mantenimiento/')),
                ('estructura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reparacion.estructura')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField(blank=True, null=True)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('En Proceso', 'En Proceso'), ('Finalizado', 'Finalizado')], max_length=50)),
                ('evidencia', models.FileField(blank=True, null=True, upload_to='trabajos/')),
                ('encargado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Reparacion.encargado')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reparacion.planmantenimiento')),
            ],
        ),
    ]
