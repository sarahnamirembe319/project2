from django.contrib.auth.models import AbstractUser
from django.db import models 

class CustomUser(AbstractUser):
    ROLE-CHOICES = (
        ('student', 'Student Intern'),
        ('workplace','Workplace Supervisor'),
        ('academic', 'Academic Supervisor'),
        ('admin', 'Internship Admin'),

    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

class InternshipPlacement(models.Model): 
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE,limit_choices_to={'role':'student'}) 
    supervisor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, limit_choices_to={'role':'workplace'})
    start_date = models.DateField()
    end_date = models.DateField()
    approved = models.BooleanField(default=False)
    
class WeeklyLog(models.Model):,
   STATUS_CHOICES = (
       ('draft', 'Draft'),
       ('submitted', 'Submitted'),
       ('approved', 'Approved'),
       ('reviewed', 'Reviewed'),

   )

    placement = models.ForeignKey(InternshipPlacement, on_delete=models.CASCADE)
    week_number = models.IntegerField()
    tasks = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft') 

class Evaluation(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    score = models.FloatField()
    comments = models.TextField()

from django.core.exceptions import ValidationError

class InternshipPlacement(models.Model):
   student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
   start_date = models.DateField()
   end_date = models.DateField()

    def clean (self):
      overlaps = InternshipPlacement.objects.filter(
            student=self.student,
            start_date__lt=self.end_date,
            end_date__gte=self.start_date
      )
      if overlaps.exists():
            raise ValidationError("This internship placement overlaps with another placement for this student.")

class WeeklyLog(models.Model):
   ...
   def clean (self):
      if self.week_number < 1 or self.week_number > 12:
         raise ValidationError("Week number must be between 1 and 12.")

      class Meta:
         unique_together = ['placement', 'week_number']     