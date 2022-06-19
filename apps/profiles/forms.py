# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        widgets = {
            "email": forms.TextInput(
                attrs={
                    "placeholder": "example@mail.com",
                    "class": "form-control",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "placeholder": "First name",
                    "class": "form-control",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "placeholder": "Last name",
                    "class": "form-control",
                }
            ),
        }
