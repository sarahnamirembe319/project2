from django.db import models


class InternshipPlacement(models.Model):
    student_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.student_name} - {self.company_name}"


class WeeklyLog(models.Model):
    week_number = models.IntegerField()
    activities = models.TextField()
    date_submitted = models.DateField()

    def __str__(self):
        return f"Week {self.week_number}"


class EvaluationCriteria(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Evaluation(models.Model):
    criteria = models.ForeignKey(
        EvaluationCriteria,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    performance_score = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return f"Evaluation - {self.performance_score}"