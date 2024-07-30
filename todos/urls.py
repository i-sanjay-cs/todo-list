from django.urls import path
from .views import task_list, add_task, update_task, delete_task, register, user_login, user_logout, home

urlpatterns = [
    path('', home, name='home'),  # Default page
    path('task_list/', task_list, name='task_list'),
    path('add/', add_task, name='add_task'),
    path('update/<int:task_id>/', update_task, name='update_task'),
    path('delete/<int:task_id>/', delete_task, name='delete_task'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
