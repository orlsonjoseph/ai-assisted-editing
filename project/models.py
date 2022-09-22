from django.db import models

from django.conf import settings
from django.contrib.auth.models import AbstractUser

from accounts.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None

    email = models.EmailField(('email address'), unique=True)
    email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email
