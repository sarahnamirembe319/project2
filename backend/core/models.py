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
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


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