# chat/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static


from . import views

app_name='chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:user_id>/', views.room, name='room'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)