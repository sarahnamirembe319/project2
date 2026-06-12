from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "message": "ILES backend is running",
        "status": "ok"
    })


urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),
    path("api/auth/", include("users_app.urls")),
    path("api/issues/", include("issues_app.urls")),
]