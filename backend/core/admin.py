from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import InternshipPlacement
from .models import WeeklyLog 
from .models import EvaluationCriteria, Evaluation 

admin.site.register(CustomUser)
admin.site.register(InternshipPlacement)
admin.site.register(WeeklyLog)
admin.site.register(EvaluationCriteria)
admin.site.register(Evaluation)
