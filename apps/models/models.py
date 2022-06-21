# -*- encoding: utf-8 -*-

from django.conf import settings
from django.db import models

# Create your models here.


class TradingModel(models.Model):
    name = models.CharField(max_length=200, default=None)
    strategy = models.CharField(max_length=200)
    parameters = models.JSONField(default=dict)
    active = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"""{self.strategy}({", ".join([f"{key}={value}" for key, value in self.parameters.items()])})"""
