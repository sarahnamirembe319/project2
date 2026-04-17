from django.urls import path
from . import views
from .views import MeView
urlpatterns = [
      path('me/', MeView.as_view())
    # Add your URL patterns here, e.g.:
    # path('list/', views.IssueListView.as_view(), name='issue-list'),
]