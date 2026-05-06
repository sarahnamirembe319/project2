# backend/InternshipPlacements_app/admin.py

from django.contrib import admin
from .models import InternshipPlacement, WeeklyLog, EvaluationCriteria, Evaluation


@admin.register(InternshipPlacement)
class InternshipPlacementAdmin(admin.ModelAdmin):
    list_display = ('id', 'student_name', 'company_name', 'start_date', 'end_date')


@admin.register(WeeklyLog)
class WeeklyLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'week_number', 'date_submitted')


@admin.register(EvaluationCriteria)
class EvaluationCriteriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('id', 'criteria', 'performance_score')