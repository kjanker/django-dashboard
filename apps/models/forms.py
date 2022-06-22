# -*- encoding: utf-8 -*-

import datetime

from django import forms
from django.db.models.fields import BLANK_CHOICE_DASH

from .models import TradingModel
from .presets import (
    currency_choices,
    metric_choices,
    strategy_choices,
    strategy_parameters,
)


class TradingModelForm(forms.ModelForm):
    class Meta:
        model = TradingModel
        fields = ["name", "strategy", "currency", "active", "metric"]
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
            "currency": forms.Select(
                choices=currency_choices,
                attrs={
                    "placeholder": "Select a currency pair",
                    "class": "form-control",
                },
            ),
            "metric": forms.Select(
                choices=metric_choices,
                attrs={
                    "placeholder": "Select a metric",
                    "class": "form-control",
                },
            ),
        }


class ParameterForm(forms.Form):
    def __init__(self, strategy: str, values: dict = {}, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, param in strategy_parameters.get(strategy, {}).items():
            name = "parameters." + name
            if param.get("dtype") == int:
                self.fields[name] = forms.IntegerField(required=True)
            elif param.get("dtype") == float:
                self.fields[name] = forms.FloatField(required=True)
            elif param.get("dtype") == str:
                self.fields[name] = forms.CharField(required=True)
            elif param.get("dtype") == bool:
                self.fields[name] = forms.BooleanField(
                    required=False, help_text="checkbox"
                )

            self.fields[name].label = param.get("label")
            self.initial[name] = param.get("default")
            self.fields[name].widget.attrs["placeholder"] = param.get("placeholder")

        for name, field in self.fields.items():
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


class BacktestingForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        attrs = {"type": "date", "class": "form-control"}
        self.fields["start"] = forms.DateField(
            widget=forms.DateInput(attrs=attrs), required=True
        )
        self.fields["end"] = forms.DateField(
            widget=forms.DateInput(attrs=attrs), required=True
        )

        self.initial["start"] = datetime.datetime(2010, 1, 1)
        self.initial["end"] = datetime.datetime.now()
