"""
Serializers for the user API View.
"""
from django.contrib.auth import get_user_model
from core.models import UserRole, User

from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from django.contrib.auth import authenticate


class UserSerializer(ModelSerializer):
    """Serializer for the user object."""
    
    class Meta:
        model = get_user_model()
        # PrivilageGroup = serializers.StringRelatedField(many=True)
        fields = ['username', 'password', 'email', 'first_name', 'middle_name', 'last_name' ]
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password."""
        return get_user_model().objects.create_user(**validated_data)

class UserRoleSerializer(ModelSerializer):

    class Meta:
        model = UserRole
        fields = '__all__'
