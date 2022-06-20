# -*- encoding: utf-8 -*-

from django import forms

from .models import TradingModel
from .strategies import choices


class TradingModelForm(forms.ModelForm):
    class Meta:
        model = TradingModel
        fields = ["name", "strategy", "parameters", "active"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Choose a name for your model",
                    "class": "form-control",
                }
            ),
            "strategy": forms.Select(
                choices=choices,
                attrs={
                    "placeholder": "Select a strategy",
                    "class": "form-control",
                },
            ),
            "parameters": forms.Textarea(
                attrs={
                    "placeholder": """{"parameter1": "value", "parameter2": ["value", "value"]}""",
                    "class": "form-control",
                }
            ),
        }
