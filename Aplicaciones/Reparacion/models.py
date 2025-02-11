from django.db import models

class Estructura(models.Model):
    ESTADO_CHOICES = [
        ('Bueno', 'Bueno'),
        ('Regular', 'Regular'),
        ('Malo', 'Malo'),
    ]

    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=255)
    fecha_construccion = models.DateField()
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='estructuras/', blank=True, null=True)  # Guarda en 'media/estructuras/'

    def __str__(self):
        return self.nombre

class Encargado(models.Model):
    nombre = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    especialidad = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    foto = models.ImageField(upload_to='fotos_encargados/', null=True, blank=True)

    def __str__(self):
        return self.nombre


class PlanMantenimiento(models.Model):
    TIPO_CHOICES = [
        ('Preventivo', 'Preventivo'),
        ('Correctivo', 'Correctivo'),
    ]
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En Proceso', 'En Proceso'),
        ('Finalizado', 'Finalizado'),
    ]

    estructura = models.ForeignKey(Estructura, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES)
    documento = models.FileField(upload_to='planes_mantenimiento/', blank=True, null=True)

    def __str__(self):
        return f"{self.tipo} - {self.estructura.nombre}"

class Trabajo(models.Model):
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('En Proceso', 'En Proceso'),
        ('Finalizado', 'Finalizado'),
    ]

    plan = models.ForeignKey(PlanMantenimiento, on_delete=models.CASCADE)
    encargado = models.ForeignKey(Encargado, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES)
    evidencia = models.FileField(upload_to='trabajos/', blank=True, null=True)

    def __str__(self):
        return f"Trabajo en {self.plan.estructura.nombre} por {self.encargado}"
    
    

