from django.db import models
from django.conf import settings

class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.user.username}"

class Supervisor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"

class InternshipPlacement(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    position_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    workplace_supervisor = models.CharField(max_length=100)
    academic_supervisor = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.company_name} - {self.position_title}"

class EvaluationCriteria(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Evaluation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE)
    criteria = models.ForeignKey(EvaluationCriteria, on_delete=models.CASCADE)
    performance_score = models.IntegerField()
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"Evaluation of {self.student}"

class WeeklyLog(models.Model):
    STATE_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    week_number = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    state = models.CharField(max_length=20, choices=STATE_CHOICES, default='Pending')
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Week {self.week_number} - {self.student}"

class Daily_log(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    weekly_log = models.ForeignKey(Weekly_log, on_delete=models.CASCADE)
    day = models.DateField()
    activity = models.TextField()
    skills_gained = models.TextField(blank=True)
    challenges = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student} - {self.day}"