from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin

from django import forms

from .models import Museo, Pais


class MuseoForm(forms.ModelForm):
    """Form definition for Museo."""

    class Meta:
      model = Museo
      fields = (
        'nombre',
        'pais',
      )
      widgets = {
        'pais': AutocompleteSelect(
          Museo._meta.get_field('pais').remote_field,
          admin.site,
          attrs={'placeholder': 'seleccionar...'},
        )
      }
