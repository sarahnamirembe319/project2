from django.urls import path
from .views import InternshipPlacementListCreateView, InternshipPlacementDetailView

urlpatterns = [
    path('', InternshipPlacementListCreateView.as_view()),
    path('<int:pk>/', InternshipPlacementDetailView.as_view()),
]