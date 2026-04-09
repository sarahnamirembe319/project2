from django.contrib.auth.models import AbstractUser
from django.db import models 

#custom user
class CustomUser(AbstractUser):
    ROLE-CHOICES = (
        ('student', 'Student Intern'),
        ('workplace','Workplace Supervisor'),
        ('academic', 'Academic Supervisor'),
        ('admin', 'Internship Admin'),

    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

 #Internship placement
class InternshipPlacement(models.Model): 
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE,limit_choices_to={'role':'student'}) 
    supervisor = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, limit_choices_to={'role':'workplace'})
    start_date = models.DateField()
    end_date = models.DateField()
    approved = models.BooleanField(default=False)
    