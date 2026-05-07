from django.urls import path
from django.http import JsonResponse
from .views import RegisterView, LoginView, LogoutView, ProfileView, MeView
from .views import RegisterView, LoginView, LogoutView, ProfileView, MeView, DebugUserView


def home(request):
    return JsonResponse({
        "message": "ILES backend is running",
        "status": "ok"
    })


urlpatterns = [
    path("", home),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('me/', MeView.as_view(), name='me'),
]