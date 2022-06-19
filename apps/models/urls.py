# -*- encoding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    # ex: /models/
    path("models/", views.all_models, name="all_models"),
    # ex: /models/new
    path("models/new", views.new_model, name="model_details"),
    # ex: /models/5/
    path("models/<int:model_id>/", views.model_details, name="model_details"),
    # ex: /models/5/
    path("models/<int:model_id>/toggle", views.toggle_model, name="toggle_model"),
]
