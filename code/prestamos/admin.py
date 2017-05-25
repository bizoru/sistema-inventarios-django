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


admin.site.register(Responsable, ResponsableAdmin)

admin.site.register(Recurso)

admin.site.register(EspacioFisico)

admin.site.register(Salon)

admin.site.register(Auditorio)

admin.site.register(Bodega)

admin.site.register(Parqueadero)

admin.site.register(EquipoElectronico)

admin.site.register(VideoBeam)

admin.site.register(Computador)

admin.site.register(Componente)

admin.site.register(Cable)

admin.site.register(PlacaElectronica)

admin.site.register(Servicio)
admin.site.register(Internet)
admin.site.register(VideoStreaming)
admin.site.register(Usuario)
admin.site.register(Prestamo)

# Register your models here.
