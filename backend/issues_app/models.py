from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class InternshipPlacement(models.Model):
    student = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="placements"
    )
    company_name = models.CharField(max_length=200)
    position_title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    workplace_supervisor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="workplace_supervised_placements"
    )
    academic_supervisor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="academic_supervised_placements"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.end_date <= self.start_date:
            raise ValidationError("End date must be after start date.")

    def __str__(self):
        return f"{self.student.username} - {self.company_name}"


class WeeklyLog(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("submitted", "Submitted"),
        ("sent_back", "Sent Back for Editing"),
        ("approved_by_supervisor", "Approved by Supervisor"),
        ("rejected_by_admin", "Rejected by Admin"),
        ("approved_by_admin", "Approved by Admin"),
    )

    placement = models.ForeignKey(
        InternshipPlacement,
        on_delete=models.CASCADE,
        related_name="weekly_logs"
    )
    week_number = models.PositiveIntegerField()
    activities = models.TextField()
    skills_learned = models.TextField(blank=True)
    challenges = models.TextField(blank=True)
    attachment = models.FileField(upload_to="weekly_logs/", null=True, blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="draft")
    supervisor_comment = models.TextField(blank=True)
    admin_comment = models.TextField(blank=True)
    submitted_at = models.DateTimeField(null=True, blank=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("placement", "week_number")

    def __str__(self):
        return f"Week {self.week_number} - {self.placement.student.username}"


class EvaluationCriteria(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.weight}%)"


class Evaluation(models.Model):
    placement = models.ForeignKey(
        InternshipPlacement,
        on_delete=models.CASCADE,
        related_name="evaluations"
    )
    evaluator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="given_evaluations"
    )
    criteria = models.ForeignKey(
        EvaluationCriteria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    score = models.DecimalField(max_digits=5, decimal_places=2)
    comments = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("placement", "evaluator", "criteria")

    def __str__(self):
        return f"{self.evaluator.username} evaluated {self.placement}"