from django.urls import path
from snippet import views

urlpatterns = [
    path('create/', views.SnippetCreate.as_view(),name='create'),
    # path('list/', views.snippet_list, name='snippet_list'),
    # path('list/<int:pk>/', views.snippet_detail,  name='snippet_detail'),
]