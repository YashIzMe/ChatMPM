from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
    path('chat/', include('chat.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)