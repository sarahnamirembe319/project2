from django.urls import path , include
from  .import views 
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('create_placement/', views.create_placement, name='create_placement'),
    path('placements/', views.placements_list, name='placement_list'),
    path('student/<int:student_id>/', views.student_placements, name='student_placements'),

    path('create_evaluation/', views.create_evaluation, name='create_evaluation'),
    path('student_evaluation/', views.student_evaluations, name='student_evaluations'),
    path('supervisor_evaluation/', views.supervisor_evaluation, name='supervisor_evaluation'),
    path('all_evaluations/', views.all_evaluations, name='all_evaluations'),
    path('evaluation_list/', views.evaluations_list, name='evaluation_list'),

    path('login/', views.login_view, name='login'),
    path('student-dashboard/', views.student_dashboard, name='student_dashboard'),
    path('supervisor-dashboard/', views.supervisor_dashboard, name='supervisor_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', views.logout_view, name='logout'),

    path('api/evaluations/', views.get_evaluation),
    path('api/create_evaluation/', views.create_evaluation_api),
    path('api/logs/', views.logs, name='logs'),
    path('api/placements/', views.placements),
    path('api/log/create/',views.create_log),
    path('api/logs/<int:id>/',views.edit_log ),
]