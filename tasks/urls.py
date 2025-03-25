from django.urls import path
from .views import create_task, assign_task, get_tasks_for_user
from django.http import JsonResponse

def tasks_home(request):
    return JsonResponse({"message": "Welcome to the Task Management API! Use /tasks/create/ to create a task."})

urlpatterns = [
    path('', tasks_home, name='tasks_home'),  # Add this line
    path('create/', create_task, name='create_task'),
    path('<int:task_id>/assign/', assign_task, name='assign_task'),
    path('user/<int:user_id>/tasks/', get_tasks_for_user, name='user_tasks'),
]
