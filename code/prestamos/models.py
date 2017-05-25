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

class Recurso(models.Model):
    nombre = models.CharField(max_length=100, null=False, default="Recurso")
    dependencia = models.IntegerField(choices=DEPENDENCIAS_CHOICES, default=0)
    responsable = models.ForeignKey(Responsable, null=False)
    @property
    def prestado(self):
        # TODO: Validate against Prestamos
        return False

class EspacioFisico(Recurso):
    localizacion = models.CharField(max_length=100, null=False, default="Loc")

class Salon(EspacioFisico):
    sillas = models.IntegerField(default=1, null=False)

class Auditorio(EspacioFisico):
    sillas = models.IntegerField(default=1, null=False)

class Bodega(EspacioFisico):
    capacidad = models.IntegerField(default=1, null=False)

class Parqueadero(EspacioFisico):
    bahias = models.IntegerField(default=1, null=False)

class EquipoElectronico(Recurso):
    referencia = models.CharField(max_length=100, null=False, default="Referencia")
    marca = models.IntegerField(choices=MARCA_CHOICES, default=0)

class VideoBeam(EquipoElectronico):
    pass

class Computador(EquipoElectronico):
    tipo = models.IntegerField(choices=COMPUTADOR_TIPO, default=0)

class Componente(Recurso):
    marca = models.IntegerField(choices=MARCA_CHOICES, default=0)

class Cable(Componente):
    tipo = models.IntegerField(choices=CABLE_TIPO, default=0)

class PlacaElectronica(Componente):
    tipo = models.IntegerField(choices=PLACA_TIPO, default=0)

class Servicio(Recurso):
    pass

class Internet(Servicio):
    velocidad = models.IntegerField(default=1, null=False)
    subred = models.CharField(max_length=100, null=False, default="Referencia")

class VideoStreaming(Servicio):
    tipo = models.IntegerField(choices=STREAMING_TIPO, default=0)


class Usuario(models.Model):
    nombre = models.CharField(max_length=100, null=False, default="Usuario")
    codigo = models.CharField(max_length=100, null=False, default="20091020077")
    telefono = models.CharField(max_length=15, null=False, default="123435")
    @property
    def prestamos_vigentes(self):
        return []


class Prestamo(models.Model):
    usuario = models.ForeignKey(Usuario, null=False)
    recurso = models.ForeignKey(Recurso, null=False)
    observaciones = models.CharField(max_length=100, null=False, default="Usuario")
    tipo = models.IntegerField(choices=PRESTAMO_TIPO, default=0, null=False)
    fecha_inicio = models.DateTimeField(verbose_name="Fecha inicio prestamo", null=False, default=django.utils.timezone.now)
    fecha_fin =  models.DateTimeField(verbose_name="Fecha fin prestamo", null=True, default=django.utils.timezone.now)
