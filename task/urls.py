"""
URL mappings for the user API.
"""

from django.urls import path

from task import views

urlpatterns = [
    path('create/', views.TaskCreateView.as_view(), name='create'),
    path('lists/', views.TaskListView.as_view(), name='task_list'),
]