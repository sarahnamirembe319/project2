from django.contrib import admin
from .models import CustomUser, InternshipPlacement, WeeklyLog, Evaluation

admin.site.register(CustomUser)
admin.site.register(InternshipPlacement)
admin.site.register(WeeklyLog)
admin.site.register(Evaluation)
