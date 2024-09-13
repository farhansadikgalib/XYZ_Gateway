from django.db import models
from django.core.exceptions import ValidationError
from app_auth.models.user import CustomUser


def validate_nid_number(value):
    if len(value) not in [10, 13, 17]:
        raise ValidationError(
            'NID number must be either 10, 13, or 17 characters long.'
        )


class AgentProfile(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='profile_user')
    full_name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    nid_number = models.CharField(
            max_length=17,
            validators=[validate_nid_number]
        )
    is_active = models.BooleanField(default=True)
    telegram_account = models.CharField(max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
