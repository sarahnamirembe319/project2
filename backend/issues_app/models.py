from django.db import models

class InternshipPlacement(models.Model):
    student_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

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