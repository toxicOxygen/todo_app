from django.urls import path
from .views import (
    HomePageView,
    TodoCreateView,
    TodoDetailView,
    TodoUpdateView,
    TodoListView,
    TodoDeleteView
)

urlpatterns = [
    path('todos/new/',TodoCreateView.as_view(),name='todo_new'),
    path('todos/',TodoListView.as_view(),name='todo_list'),
    path('todos/<int:pk>/edit/',TodoUpdateView.as_view(),name='todo_edit'),
    path('todos/<int:pk>/delete/',TodoDeleteView.as_view(),name='todo_delete'),
    path('todos/<int:pk>/',TodoDetailView.as_view(),name='todo_detail'),
    path('',HomePageView.as_view(),name='home')
]