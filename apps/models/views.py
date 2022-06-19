# -*- encoding: utf-8 -*-

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

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
def model_details(request, model_id=None):
    model = TradingModel.objects.filter(id=model_id)[0] if model_id else None
    msg = None
    editable = request.user == model.owner

    if request.method == "POST" and editable:
        form = TradingModelForm(request.POST, instance=model)
        if form.is_valid():
            form.save()
            msg = "Changes to the model have been saved!"
        else:
            msg = "Error: Could not save model!"
    else:
        form = TradingModelForm(instance=model)

    context = {
        "segment": "all-models",
        "model": model,
        "form": form,
        "msg": msg,
        "editable": editable,
    }

    return render(request, "models/single-model.html", context)


@login_required(login_url="/login/")
def new_model(request):
    msg = None

    if request.method == "POST":
        form = TradingModelForm(request.POST, initial={"owner_id": request.user})
        if form.is_valid():
            model = form.save(commit=False)
            model.owner = request.user
            model.save()
            return redirect("model_details", model_id=model.id)
        else:
            msg = "Error: Could not save model!"
    else:
        form = TradingModelForm()

    context = {"segment": "all-models", "form": form, "msg": msg, "new": True}

    return render(request, "models/single-model.html", context)


@login_required(login_url="/login/")
def toggle_model(request, model_id):
    model = TradingModel.objects.filter(id=model_id)[0]
    if request.user == model.owner:
        model.active = not model.active
        model.save()
    return all_models(request)
