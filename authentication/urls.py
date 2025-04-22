"""
URL mappings for the user API.
"""
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView  
)
from django.urls import path

from authentication import views


app_name = 'authentication'

urlpatterns = [
    path('authenticate/', views.LoginRequest.as_view(), name="token_obtain_pair"),
]