# -*- encoding: utf-8 -*-

from django.urls import path, re_path

from . import views

urlpatterns = [
    # ex: /profile
    path("profile", views.user_profile, name="user_profile"),
    # ex: /user/admin
    path("user/<str:username>", views.user_profile, name="user_profile"),
]
