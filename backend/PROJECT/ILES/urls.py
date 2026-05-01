from django.urls import path
from . import views

urlpatterns = [
    # Template views
    path('placements/', views.placements_list, name='placements_list'),
    path('placements/create/', views.create_placement, name='create_placement'),
    path('placements/<int:student_id>/', views.student_placements, name='student_placements'),
    path('evaluations/', views.evaluations_list, name='evaluations_list'),
    path('evaluations/create/', views.create_evaluation, name='create_evaluation'),
    path('evaluations/student/', views.student_evaluations, name='student_evaluations'),
    path('evaluations/supervisor/', views.supervisor_evaluation, name='supervisor_evaluation'),
    path('evaluations/all/', views.all_evaluations, name='all_evaluations'),
    path('logs/daily/create/', views.create_daily_log, name='create_daily_log'),
    path('logs/daily/', views.daily_logs_list, name='daily_logs_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    path('dashboard/supervisor/', views.supervisor_dashboard, name='supervisor_dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # API views
    path('api/evaluations/', views.create_evaluation_api, name='create_evaluation_api'),
    path('api/evaluations/list/', views.get_evaluation, name='get_evaluation'),
    path('api/placements/', views.placements, name='placements_api'),
    path('api/logs/', views.logs, name='logs'),
    path('api/logs/create/', views.create_log, name='create_log'),
    path('api/logs/<int:id>/edit/', views.edit_log, name='edit_log'),
    path('api/logs/<int:pk>/update/', views.update_log, name='update_log'),
]