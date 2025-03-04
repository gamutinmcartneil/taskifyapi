from django.shortcuts import render

from rest_framework import generics
from task.serializers import TaskViewSerializer, TaskCreateSerializer
from core.models import Task
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class TaskCreateView(generics.CreateAPIView):
    serializer_class = TaskCreateSerializer


class TaskListView(generics.ListAPIView):
    serializer_class = TaskViewSerializer
    queryset = Task.objects.all()
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

