from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # auth routes
    path('api/auth/', include('users_app.urls')),

    # issues routes
    path('api/issues/', include('issues_app.urls')),
]