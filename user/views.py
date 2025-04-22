from django.shortcuts import render


from user.serializers import UserSerializer

from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view

class CreateUserView(CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer

@api_view(['POST'])
def validate_token(request):
    token = request.data.get('token')
    authenticator = JWTAuthentication()
    try:
        authenticator.get_validated_token(token)
        return Response({"valid": True}, status=200)
    except Exception:
        return Response({"valid": False}, status=401)
    

class ManageUserView(RetrieveUpdateAPIView):
    """Manage the authenticated user."""
   
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user

