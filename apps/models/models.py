# -*- encoding: utf-8 -*-

from django.conf import settings
from django.db import models

# Create your models here.


class TradingModel(models.Model):
    name = models.CharField(max_length=150, default=None)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    strategy = models.CharField(max_length=150)
    parameters = models.JSONField(default=dict)
    currency = models.CharField(max_length=50, default="ETH/BTC")
    active = models.BooleanField(default=False)
    metric = models.CharField(max_length=50, default="TotalReturn")

    def __str__(self):
        return f"""{self.strategy}({", ".join([f"{key}={value}" for key, value in self.parameters.items()])})"""
