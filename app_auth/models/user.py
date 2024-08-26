from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Group, Permission
from django.db import models


# app_auth/models.py
class CustomUserManager(BaseUserManager):
    def create_user(self, login, password=None, **extra_fields):
        print(extra_fields)
        if not login:
            raise ValueError('The Login field must be set')
        user = self.model(login=login, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, login, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self.create_user(login, password, **extra_fields)
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    write_date = models.DateTimeField(auto_now=True)
    create_uid = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='created_users')
    write_uid = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name='written_users')
    is_staff = models.BooleanField(default=False)  # Add this field
    is_active = models.BooleanField(default=True)  # This field is also often required

    objects = CustomUserManager()
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.name

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Custom related name to avoid clash
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',  # Custom related name to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def save(self, *args, **kwargs):
        self.set_password(self.password)
        return super().save(self, *args, **kwargs)

