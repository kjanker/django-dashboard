# -*- encoding: utf-8 -*-

import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import BacktestingForm, ParameterForm, TradingModelForm
from .models import TradingModel


@login_required(login_url="/login/")
def all_models(request):
    context = {
        "segment": "all-models",
        "models": TradingModel.objects.order_by("id"),
    }
    return render(request, "models/all-models.html", context)


@login_required(login_url="/login/")
def model_details(request, model_id):
    model = TradingModel.objects.filter(id=model_id)[0]
    msg = None
    editable = request.user == model.owner

    if request.POST.get("backtest"):
        backtesting_form = BacktestingForm(request.POST)
        if backtesting_form.is_valid():
            logging.info(f"trigger backtesting of model {model.id}.")
            pass
    else:
        backtesting_form = BacktestingForm()

    if editable and request.POST.get("delete"):
        """Delete button pressed"""
        model.delete()
        return redirect("all_models")
    elif editable and request.POST.get("save"):
        """Save button pressed"""
        data = request.POST.copy()
        data["strategy"] = model.strategy
        form = TradingModelForm(data=data, instance=model)
        if form.is_valid():
            model: TradingModel = form.save(commit=False)
            model.parameters = ParameterForm.get_params(
                request.POST, strategy=model.strategy
            )
            model.save()
            msg = "Changes to the model have been saved!"
        else:
            msg = "Error: Could not save model!"
    else:
        form = TradingModelForm(instance=model)

    parameter_form = ParameterForm(
        strategy=request.POST.get("strategy", model.strategy),
        values=model.parameters,
    )

    if not editable:
        for _, field in form.fields.items():
            field.widget.attrs["disabled"] = True

    form.fields["strategy"].disabled = True

    context = {
        "segment": "all-models",
        "model": model,
        "form": form,
        "parameters": parameter_form,
        "msg": msg,
        "editable": editable,
        "backtesting": backtesting_form,
    }

    return render(request, "models/single-model.html", context)


@login_required(login_url="/login/")
def new_model(request):
    msg = None

    if request.method == "POST":
        if request.POST.get("create"):
            """Create button pressed"""
            form = TradingModelForm(request.POST, initial={"owner_id": request.user})
            if form.is_valid():
                model = form.save(commit=False)
                model.owner = request.user
                model.parameters = ParameterForm.get_params(request.POST)
                model.save()
                return redirect("model_details", model_id=model.id)
            else:
                msg = "Error: Could not save model!"
        else:
            """Strategy changed"""
            form = TradingModelForm(request.POST, initial={"owner_id": request.user})
    else:
        form = TradingModelForm(initial={"strategy": None})

    parameter_form = ParameterForm(
        strategy=request.POST.get("strategy", ""),
    )

    context = {
        "segment": "all-models",
        "form": form,
        "parameters": parameter_form,
        "msg": msg,
        "create": True,
    }

    return render(request, "models/single-model.html", context)


@login_required(login_url="/login/")
def toggle_model(request, model_id):
    model = TradingModel.objects.filter(id=model_id)[0]
    if request.user == model.owner:
        model.active = not model.active
        model.save()
    return redirect("all_models")
