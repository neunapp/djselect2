from django.shortcuts import render
#
from django.views.generic import CreateView
#
from .models import Museo
#
from .forms import MuseoForm


class MuseoCreateView(CreateView):
    model = Museo
    template_name = "museo/add.html"
    form_class = MuseoForm
    success_url = '.'

