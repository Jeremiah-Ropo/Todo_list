from django.urls import path
from .views import TaskCreate, DeleteView, TaskDetail, RegisterView, TaskList, TaskUpdate, CustomLoginView
from django.contrib.auth.views import LogoutView

app_name = 'base'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='base:login'),name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task_update'),
    path('task-delete/<int:pk>/', DeleteView.as_view(), name='task_delete'),

]
