from django.urls import path

from . import views

urlpatterns = [
    path('SignUp', views.register_view, name='register'),
]
