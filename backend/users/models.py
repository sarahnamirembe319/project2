from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        DEVELOPER = 'developer', 'Developer'
        SUBMITTER = 'submitter', 'Submitter'

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.SUBMITTER,
    )

    def __str__(self):
        return f'{self.username} ({self.role})'
