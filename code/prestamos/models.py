# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django

DEPENDENCIAS_CHOICES = (
    (0, "Ingenieria"),
    (1, "Laboratorios"),
    (2, "Biblioteca")
)

MARCA_CHOICES = (
    (0, "Daweo"),
    (1, "LG"),
    (2, "Sony")
)

COMPUTADOR_TIPO = (
    (0, "Portatil"),
    (1, "Escritorio")
)

CABLE_TIPO = (
    (0, "HDMI"),
    (1, "VGA")
)

PLACA_TIPO = (
    (0, "A"),
    (1, "B")
)
STREAMING_TIPO = (
    (0, "Youtube"),
    (1, "Otro")
)
PRESTAMO_TIPO = (
    (0, "Local"),
    (1, "Remoto")
)


# Create your models here.

class Responsable(models.Model):
    nombre = models.CharField(max_length=100, null=False, default="")
    correo = models.CharField(max_length=100, null=False, default="", unique=True)
    telefono = models.CharField(max_length=100, null=False, default="")

    def __str__(self):
        return self.nombre

class Recurso(models.Model):
    nombre = models.CharField(max_length=100, null=False, default="Recurso")
    dependencia = models.IntegerField(choices=DEPENDENCIAS_CHOICES, default=0)
    responsable = models.ForeignKey(Responsable, null=False)

    def prestado(self):
        return Prestamo.objects.filter(recurso_id=self.pk).exists()

    def disponible(self):
        if Prestamo.objects.filter(recurso_id=self.pk).exists():
            prestamo = Prestamo.objects.filter(recurso_id=self.pk).get()
            return "Prestado a {}".format(prestamo.usuario)
        return "Disponible para prestamo"


    def __str__(self):
        if self.prestado():
            return "{} (Prestado)".format(self.nombre)
        return self.nombre


class EspacioFisico(Recurso):
    localizacion = models.CharField(max_length=100, null=False, default="Loc",verbose_name="Localizacion Fisica")

class Salon(EspacioFisico):
    sillas = models.IntegerField(default=1, null=False,verbose_name="Cantidad de Sillas Disponibles")
    class Meta:
        verbose_name_plural = "Salones"

class Auditorio(EspacioFisico):
    sillas = models.IntegerField(default=1, null=False, verbose_name="Cantidad de Sillas Disponibles")

class Bodega(EspacioFisico):
    capacidad = models.IntegerField(default=1, null=False, verbose_name="Capacidad Volumetrica")

class Parqueadero(EspacioFisico):
    bahias = models.IntegerField(default=1, null=False,verbose_name="Cantidad de Bahias Disponibles")

class EquipoElectronico(Recurso):
    referencia = models.CharField(max_length=100, null=False, default="Referencia")
    marca = models.IntegerField(choices=MARCA_CHOICES, default=0)

class VideoBeam(EquipoElectronico):
    pass

class Computador(EquipoElectronico):
    tipo = models.IntegerField(choices=COMPUTADOR_TIPO, default=0)
    class Meta:
        verbose_name_plural = "Computadores"

class Componente(Recurso):
    marca = models.IntegerField(choices=MARCA_CHOICES, default=0)

class Cable(Componente):
    tipo = models.IntegerField(choices=CABLE_TIPO, default=0)
    def save_model(self, request, obj, form, change):
        obj.cable = request.cable
        obj.save()

class PlacaElectronica(Componente):
    tipo = models.IntegerField(choices=PLACA_TIPO, default=0)
    class Meta:
        verbose_name_plural = "Placas Electronicas"

class Servicio(Recurso):
    pass

class Internet(Servicio):
    velocidad = models.IntegerField(default=1, null=False,verbose_name="Velocidad en MB/s")
    subred = models.CharField(max_length=100, null=False, default="Referencia",verbose_name="Subred Logica")
    class Meta:
        verbose_name_plural = "Servicios de Internet"

class VideoStreaming(Servicio):
    tipo = models.IntegerField(choices=STREAMING_TIPO, default=0)
    class Meta:
        verbose_name_plural = "Servicio de Video Streaming"


class Usuario(models.Model):
    nombre = models.CharField(max_length=100, null=False, default="Usuario")
    codigo = models.CharField(max_length=100, null=False, default="20091020077")
    telefono = models.CharField(max_length=15, null=False, default="123435")
    @property
    def prestamos_vigentes(self):
        return []
    def __str__(self):
        return self.nombre


class Prestamo(models.Model):
    usuario = models.ForeignKey(Usuario, null=False)
    recurso = models.ForeignKey(Recurso, null=False, unique=True)
    observaciones = models.CharField(max_length=100, null=False, default="Usuario")
    tipo = models.IntegerField(choices=PRESTAMO_TIPO, default=0, null=False)
    fecha_inicio = models.DateTimeField(verbose_name="Fecha inicio prestamo", null=False, default=django.utils.timezone.now)
    fecha_fin =  models.DateTimeField(verbose_name="Fecha fin prestamo", null=True, default=django.utils.timezone.now)
    def __str__(self):
        return "Prestamo del Recurso {} al usuario {}".format(self.recurso,self.usuario)
