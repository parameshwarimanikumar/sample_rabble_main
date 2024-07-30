from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.views import account_list, api_response  # Import account_list view

urlpatterns = [
    path('accounts/', account_list, name='account_list'),
    path('api-response/', api_response, name='api_response'),  # Remove '.html' from the name
    path('admin/', admin.site.urls),
    path('auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('api/', include('apps.api.urls')),
    path('accounts/', account_list, name='account_list'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
