"""
Serializers for the user API View.
"""
from core.models import Task, Priority

from rest_framework import serializers
from user.serializers import UserSerializer


class Priority(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = '__all__'

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'assignedto', 'priority', 'description')
        
    def create(self, validated_data):
        return Task.objects.create(**validated_data)

class TaskViewSerializer(serializers.ModelSerializer):
    """Serializer for the task object."""
    assignedto = UserSerializer()
    priority = Priority()
    
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'priority', 'assignedto')

    

