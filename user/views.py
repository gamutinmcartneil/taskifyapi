from django.shortcuts import render

# Create your views here.
"""
Views for the user API.
"""
import datetime

from django.http import JsonResponse

from user.serializers import UserSerializer

from rest_framework import generics
from rest_framework.generics import GenericAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView


class CreateUserView(CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer

class ManageUserView(RetrieveUpdateAPIView):
    """Manage the authenticated user."""
   
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user
    
@api_view(['POST'])
def validate_token(request):
    token = request.data.get('token')
    authenticator = JWTAuthentication()
    try:
        authenticator.get_validated_token(token)
        return Response({"valid": True}, status=200)
    except Exception:
        return Response({"valid": False}, status=401)


class CustomTokenObtainView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        token_response = super().post(request, *args, **kwargs)
        
        # Assuming token_response is a Response object
        token_data = token_response.data
        # Set session cookie
        request.session['token'] = token_data['access']
        # Combine the responses as needed
        combined_data = {
            'token': token_data,
        }
        
        return JsonResponse(combined_data)

