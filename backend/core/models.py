from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings 
#from internships.models import InternshipPlacement

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
        if self.role not in dict(self.ROLE_CHOICES):
            raise ValidationError({'role': 'Invalid role selected.'})
        

    
              

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
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('reviewed', 'Reviewed'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    placement = models.ForeignKey(
        InternshipPlacement,
        on_delete=models.CASCADE,
        related_name='weekly_logs'
    )
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='weekly_logs'
    )
    week_number = models.IntegerField()
    activities = models.TextField()
    skills_learned = models.TextField(blank=True)
    challenges = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )
    submitted_at = models.DateTimeField(auto_now_add=True)
    supervisor_comment = models.TextField(blank=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['placement', 'week_number']  # one log per week

    def __str__(self):
        return f"Week {self.week_number} log - {self.student.username}"


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
    
class InternshipPlacement(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='placements'
    )
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.student.username} - {self.company}"
    
    def clean(self):
     if self.start_date and self.end_date:
      if self.end_date <= self.start_date:
                raise ValidationError("End date must be after start date.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)