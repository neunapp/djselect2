from django.contrib import admin
#
from .models import Pais, Museo


class PaisAdmin(admin.ModelAdmin):
    search_fields = ('nombre'),
    ordering = ['nombre']


class MuseoAdmin(admin.ModelAdmin):
    ordering = ['nombre']
    autocomplete_fields = ['pais']


admin.site.register(Pais, PaisAdmin)
admin.site.register(Museo, MuseoAdmin)
