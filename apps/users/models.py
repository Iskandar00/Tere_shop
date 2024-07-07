from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class CustomUser(AbstractUser):
    admin = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.admin = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username