from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student Intern'),
        ('workplace', 'Workplace Supervisor'),
        ('academic', 'Academic Supervisor'),
        ('admin', 'Internship Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_set',
        related_query_name='custom_user',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_set',
        related_query_name='custom_user',
    )


class WeeklyLog(models.Model):
    week_number = models.IntegerField()
    activities = models.TextField()
    date_submitted = models.DateField()

class EvaluationCriteria(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Evaluation(models.Model):
    score = models.IntegerField()
    comments = models.TextField()

# ... (rest of your models remain the same)