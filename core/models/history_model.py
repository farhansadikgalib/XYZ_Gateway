# mixins.py
from django.db import models
from simple_history.models import HistoricalRecords

class HistoryMixin(models.Model):
    history = HistoricalRecords()

    class Meta:
        abstract = True
