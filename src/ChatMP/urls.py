from django.contrib import admin
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path

from accounts.views import (
    register_view,
    login_view,
    logout_view,
 
)

urlpatterns = [
    path('chat/', include('chat.urls',namespace='chat'), name='chat'),
    path('admin/', admin.site.urls),
    path('', include('accounts.urls',namespace='accounts'), name='accounts'),
    ]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)