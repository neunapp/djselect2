#
from django.urls import path

from . import views

app_name = "museo_app"

urlpatterns = [
    path(
        '',
        views.MuseoCreateView.as_view(),
        name='museo-add'
    ),
]