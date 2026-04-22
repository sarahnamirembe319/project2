"""
URL configuration for iles_backend project.
"""
from django.contrib import admin
from django.urls import path, include
from users_app.views import MeView

urlpatterns = [
    path('', lambda request: HttpResponse("API is working 🚀")),
    path('admin/', admin.site.urls),
    path('issues/', include('issues_app.urls')),
    path('users/', include('users_app.urls')),
    path('me/', MeView.as_view()),
]