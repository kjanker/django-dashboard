# -*- encoding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import TradingModelForm
from .models import TradingModel


@login_required(login_url="/login/")
def all_models(request):
    context = {
        "segment": "all-models",
        "models": TradingModel.objects.order_by("id"),
    }
    return render(request, "models/all-models.html", context)


@login_required(login_url="/login/")
def model_details(request, strategy_id):
    model = TradingModel.objects.filter(id=strategy_id)[0]
    msg = None

    if request.method == "POST" and request.user == model.owner:
        form = TradingModelForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
            msg = "Changes to the model have been saved!"
        else:
            msg = f"Error: Could not save model!"
    else:
        form = TradingModelForm(instance=model)

    context = {"segment": "all-models", "model": model, "form": form, "msg": msg}

    return render(request, "models/single-model.html", context)


@login_required(login_url="/login/")
def toggle_model(request, strategy_id):
    model = TradingModel.objects.filter(id=strategy_id)[0]
    if request.user == model.owner:
        model.active = not model.active
        model.save()
    return all_models(request)
