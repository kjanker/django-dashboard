# -*- encoding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    # ex: /models/
    path("models/", views.all_models, name="all_models"),
    # ex: /models/5/
    path("models/<int:strategy_id>/", views.model_details, name="model_details"),
    # ex: /models/5/
    path("models/<int:strategy_id>/toggle", views.toggle_model, name="toggle_model"),
]
