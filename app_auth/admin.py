from django.contrib import admin
from app_auth.models.user import CustomUser

# Register your models here.
admin.site.register(CustomUser)
