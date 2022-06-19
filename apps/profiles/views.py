# -*- encoding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserForm


@login_required(login_url="/login/")
def user_profile(request, username=None):
    if username is None:
        return redirect("user/" + request.user.username)

    user = get_user_model().objects.filter(username=username)[0]
    msg = None
    editable = request.user == user

    if request.method == "POST" and editable:
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            msg = "Changes to your profile have been saved!"
        else:
            msg = f"Error: Could not save changes!"
    else:
        form = UserForm(instance=user)

    if not editable:
        for _, field in form.fields.items():
            field.widget.attrs["disabled"] = True

    context = {
        "segment": "user",
        "user": user,
        "form": form,
        "msg": msg,
        "editable": editable,
    }

    return render(request, "profiles/user-profile.html", context)
