from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', lambda request: HttpResponse("API is working 🚀")),
    path('admin/', admin.site.urls),
    path('api/auth/', include('issues_app.urls')),
    path('api/issues/', include('issues_app.urls')),
    path('api/users/', include('users_app.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)