# -*- encoding: utf-8 -*-

from django import forms

from .models import TradingModel


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
            "strategy": forms.TextInput(
                attrs={
                    "placeholder": "Select a strategy",
                    "class": "form-control",
                }
            ),
            "parameters": forms.Textarea(
                attrs={
                    "placeholder": """{"parameter1": "value", "parameter2": ["value", "value"]}""",
                    "class": "form-control",
                }
            ),
        }
