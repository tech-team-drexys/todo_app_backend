from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health_check, name='health'),
    path('todos/', views.TodoListCreateView.as_view(), name='todo-list'),
    path('todos/<int:pk>/', views.TodoDetailView.as_view(), name='todo-detail'),
]