from datetime import datetime

from django.db import models
from simple_history.models import HistoricalRecords
from django.forms.models import model_to_dict
from app_auth.models.user import CustomUser


class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=False)


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL,
                                   null=True, related_name='%(class)s_created')
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL,
                                   null=True, related_name='%(class)s_updated')

    is_active = models.BooleanField(default=False)
    version = models.IntegerField(default=1)

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    history = HistoricalRecords(inherit=True)

    def soft_delete(self, update_user=None):
        self.is_active = True
        if update_user is not None:
            self.updated_by = update_user
        self.save()
