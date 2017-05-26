# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

class ResponsableAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'correo',
        'telefono'
    )


class CableAdmin(admin.ModelAdmin):
    list_display = ('tipo','marca','dependencia','responsable','disponible')

class SalonAdmin(admin.ModelAdmin):
    list_display = ('nombre','dependencia','localizacion','sillas','disponible')

class AuditorioAdmin(admin.ModelAdmin):
    list_display = ('nombre','dependencia','localizacion','sillas','disponible')

class BodegaAdmin(admin.ModelAdmin):
    list_display = ('nombre','dependencia','localizacion','capacidad','disponible')

class ParqueaderoAdmin(admin.ModelAdmin):
    list_display = ('nombre','dependencia','localizacion','bahias','disponible')

class VideoBeamAdmin(admin.ModelAdmin):
    list_display = ('nombre','referencia','marca','dependencia','disponible')

class ComputadorAdmin(admin.ModelAdmin):
    list_display = ('nombre','referencia','marca','tipo','dependencia','disponible')

class PlacaElectronicaAdmin(admin.ModelAdmin):
    list_display = ('nombre','marca','dependencia','tipo','disponible')

class InternetAdmin(admin.ModelAdmin):
    list_display = ('nombre','velocidad','subred','dependencia','disponible')

class VideoStreamingAdmin(admin.ModelAdmin):
    list_display = ('nombre','tipo','dependencia','disponible')

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('usuario','recurso','observaciones','tipo','fecha_inicio','fecha_fin')

admin.site.register(Responsable, ResponsableAdmin)
admin.site.register(Salon, SalonAdmin)
admin.site.register(Auditorio, AuditorioAdmin)
admin.site.register(Bodega, BodegaAdmin)
admin.site.register(Parqueadero, ParqueaderoAdmin)
admin.site.register(VideoBeam, VideoBeamAdmin)
admin.site.register(Computador, ComputadorAdmin)
admin.site.register(Cable, CableAdmin)
admin.site.register(PlacaElectronica, PlacaElectronicaAdmin)
admin.site.register(Internet, InternetAdmin)
admin.site.register(VideoStreaming,VideoStreamingAdmin)
admin.site.register(Usuario)
admin.site.register(Prestamo,PrestamoAdmin)
