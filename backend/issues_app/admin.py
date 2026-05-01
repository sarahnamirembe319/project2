from django.contrib import admin
from .models import Internship_placement, Weekly_log, Evaluation_criteria, Evaluation, Student, Supervisor, Daily_log

admin.site.register(Internship_placement)
admin.site.register(Weekly_log)
admin.site.register(Evaluation_criteria)
admin.site.register(Evaluation)
admin.site.register(Student)
admin.site.register(Supervisor)
admin.site.register(Daily_log)