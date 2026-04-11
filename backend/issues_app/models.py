from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.
class CustomUser(AbstractUser):
    student='student'
    supervisor='supervisor'
    admin='admin'
    ROLE_CHOICES=[
        ('student','Student'),
        ('supervisor','Supervisor'),
        ('admin','Admin')
    ]

    role=models.CharField(max_length=30,blank=True,null=True,choices=ROLE_CHOICES)
    department=models.CharField(max_length=30,blank=True,null=True)
    startdate=models.DateField(blank=True,null=True)
    end_date=models.DateField(blank=True,null=True)
class Student(models.Model):
    user=models.OneToOneField(CustomUser, on_delete=models.CASCADE)

class Weekly_log(models.Model):
    STATE_CHOICES=[
        ('Draft','Draft'),
        ('submitted','submitted'),
        ('Reviewed','Reviewed'),
        ('Approved','Approved'),
        ('Rejected','Rejected'),
    ]
    week_number=models.PositiveIntegerField()
    start_date=models.DateField()
    end_date=models.DateField()
    state=models.CharField(max_length=10,choices=STATE_CHOICES,default='Draft')
    student=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="student_weekly_logs")# FOREIGN KEY: Each log MUST belong to a student
    supervisor=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="supervisor_weekly_logs")
    def __str__(self):
        return f"{self.student.username}- week{self.week_number}"
    
class Daily_log(models.Model):
    DAY_CHOICES=[
        ('mon','monday'),
        ('tue','tuesday'),
        ('wed','wednesday'),
        ('thur','thursday'),
        ('fri','friday'),
    ]
    weekly_log=models.ForeignKey(Weekly_log,on_delete=models.CASCADE,related_name='daily_entries')
    student=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="daily_logs")
    day=models.CharField(max_length=4,blank=True, null=True,choices=DAY_CHOICES)
    activity=models.CharField(max_length=255,blank=True, null=True)
    skills_gained=models.CharField(max_length=255,blank=True, null=True)
    challenges=models.TextField(blank=True,null=True)
    description=models.TextField(blank=True, null=True)
    supervisor_comments=models.TextField(blank=True, null=True)
    
class Supervisor(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="supervisor_profile")# ONE-TO-ONE: Every Supervisor is linked to exactly one User account
    department = models.CharField(max_length=30, blank =True , null= True)
    company_name= models.CharField(max_length=100, blank = True , null=True)

class Internship_placement(models.Model):
    student=models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="placements") # FOREIGN KEY: Many placements can belong to one Student (User)
    position_title=models.CharField(max_length=50)
    company_name=models.CharField(max_length=50)
    start_date=models.DateField()
    end_date=models.DateField()
    workplace_supervisor=models.CharField(max_length=50)
    academic_supervisor=models.CharField(max_length=50)
    submitted_at=models.DateTimeField(default=timezone.now)


    class Meta(): #defines extra settings 
        ordering =['-submitted_at'] #order by submission date ie controls default order of records
        unique_together =['student','company_name','position_title']# enforcess uniqueness
    
    def __str__(self):
        return f"{self.student_name}-{self.position_title} @{self.company_name}"
    
class Evaluation_criteria(models.Model):
    criteria_name=models.CharField(max_length=100)
    description =models.TextField(blank= True , null=True)    

class Evaluation(models.Model):
    student=models.ForeignKey(CustomUser, on_delete=models.CASCADE ,related_name="received_evaluations")# FOREIGN KEY: Links the result to the Student and the Supervisor
    supervisor=models.ForeignKey(Supervisor ,on_delete=models.CASCADE,related_name="given_evaluations")
    date_submitted = models.DateField(auto_now_add=True)
    criteria=models.ForeignKey(Evaluation_criteria, on_delete=models.CASCADE)
    performance_score = models.IntegerField()
    comments= models.TextField(blank=True, null= True)

    class Meta:
        unique_together=('student', 'criteria')

    def __str__(self):
        return f"{self.student.name}-{self.criteria.criteria_name} : {self.performance_score}"
