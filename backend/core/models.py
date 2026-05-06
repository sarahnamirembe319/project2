from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("student", "Student Intern"),
        ("workplace", "Workplace Supervisor"),
        ("academic", "Academic Supervisor"),
        ("admin", "Internship Admin"),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="student"
    )

    def __str__(self):
        return f"{self.username} ({self.role})"