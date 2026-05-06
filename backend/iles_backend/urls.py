from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf.urls.static import static
from django.conf import settings
from users_app.views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', lambda request: HttpResponse("API is working 🚀")),
    path('api/auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('InternshipPlacements_app.urls')),
    path('api/InternshipPlacements/', include('InternshipPlacements_app.urls')),
    path('api/users/', include('users_app.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)