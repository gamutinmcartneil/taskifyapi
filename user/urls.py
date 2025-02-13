"""
URL mappings for the user API.
"""
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView  
)
from django.urls import path

from user import views


app_name = 'user'

urlpatterns = [
    # path('create/', views.CreateUserView.as_view(), name='create'),
    # path('jwt/token/', views.CustomTokenObtainView.as_view(), name='token_obtain_pair'),
    # path('jwt/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    # path('me/', views.ManageUserView.as_view(), name="me"),
    # path('logout/', views.LogoutView.as_view(), name='logout'),
    
]