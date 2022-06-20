# -*- encoding: utf-8 -*-

from django import forms
from django.db.models.fields import BLANK_CHOICE_DASH

from .models import TradingModel
from .strategies import choices as strategy_choices
from .strategies import parameters as strategy_parameters


class TradingModelForm(forms.ModelForm):
    class Meta:
        model = TradingModel
        fields = ["name", "strategy", "active"]
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Choose a name for your model",
                    "class": "form-control",
                }
            ),
            "strategy": forms.Select(
                choices=BLANK_CHOICE_DASH + strategy_choices,
                attrs={
                    "placeholder": "Select a strategy",
                    "class": "form-control",
                    "onChange": "form.submit();",
                },
            ),
        }


class ParameterForm(forms.Form):
    def __init__(self, strategy: str, values: dict = {}, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, type in strategy_parameters.get(strategy, {}).items():
            name = "parameters." + name
            if type == int:
                self.fields[name] = forms.IntegerField(required=True)
            elif type == float:
                self.fields[name] = forms.FloatField(required=True)
            elif type == str:
                self.fields[name] = forms.CharField(required=True)
            elif type == bool:
                self.fields[name] = forms.BooleanField(required=False)

        for name, field in self.fields.items():
            field.widget.attrs["placeholder"] = name + " value"
            field.widget.attrs["class"] = "form-control"

        for name, value in values.items():
            name = "parameters." + name
            self.initial[name] = value

    def get_params(POST, strategy=None):
        strategy = strategy or POST.get("strategy")
        params = {}
        for key, _ in strategy_parameters.get(strategy, {}).items():
            params[key] = POST.get("parameters." + key)
        return params
