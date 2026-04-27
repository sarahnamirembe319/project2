from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.config import settings 

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
    def clean(self):
        super().clean()
        if self.role not in dict(self.ROLE_CHOICES)->sel-

class EvaluationCriteria(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)  # e.g. 40.00

    def __str__(self):
        return f"{self.name} ({self.weight}%)"


class Evaluation(models.Model):
    EVALUATOR_TYPE_CHOICES = [
        ('workplace', 'Workplace Supervisor'),
        ('academic', 'Academic Supervisor'),
    ]

    placement = models.ForeignKey(
        InternshipPlacement,
        on_delete=models.CASCADE,
        related_name='evaluations'
    )
    evaluator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='given_evaluations'
    )
    evaluator_type = models.CharField(
        max_length=20,
        choices=EVALUATOR_TYPE_CHOICES
    )
    criteria = models.ForeignKey(
        EvaluationCriteria,
        on_delete=models.CASCADE
    )
    score = models.DecimalField(max_digits=5, decimal_places=2)  # out of 100
    comments = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # prevent duplicate evaluations
        unique_together = ['placement', 'evaluator', 'criteria']

    def __str__(self):
        return f"{self.evaluator.username} evaluated {self.placement}"

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

