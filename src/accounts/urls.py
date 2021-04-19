from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('SignUp', views.register_view, name='register'),
    path('Login', views.login_view, name='login'),
    path('Logout', views.logout_view, name='logout'),
    path('<user_id>/', views.account_view, name="view"),
]
